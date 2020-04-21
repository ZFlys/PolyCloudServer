import json
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from PolyCloudService.models import User
from django.core.exceptions import ObjectDoesNotExist
import hashlib
from PolyCloudService import models
from django.core import serializers
from django.db.models import F
import random
import requests


def hash_code(s, salt='scutpoly'):
    h = hashlib.sha256()
    s += salt
    h.update(s.encode())
    return h.hexdigest()


def app_service(request):
    return HttpResponse("PolyCloudApp Service!")


def login(request):
    username = request.POST.get('username')
    password = request.POST.get('password')
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        status = "用户未注册"
    else:
        if user.password == hash_code(password):
            status = "验证成功"
        else:
            status = "验证失败"
    result = {'status': status}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def register(request):
    username = request.POST.get('username')
    password = request.POST.get('password')

    # 删除空记录
    try:
        null_user = User.objects.get(username='')
        null_user.delete()
    except ObjectDoesNotExist:
        pass

    try:
        User.objects.get(username=username)
        message = 'userExisted'
    except ObjectDoesNotExist:
        new_user = User.objects.create()
        new_user.username = username
        new_user.password = hash_code(password)
        new_user.privilege = 'common'
        try:
            new_user.save()
            message = 'registerSuccess'
        except Exception as e:
            print(e)
            message = 'registerError'
    result = {'message': message}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def change_password(request):
    username = request.POST.get('username')
    old_password = request.POST.get('oldPassword')
    new_password = request.POST.get('newPassword')
    if username == "":
        status = "userInfoError"
    try:
        user = User.objects.get(username=username)
    except ObjectDoesNotExist:
        status = "userInfoError"
    else:
        if user.password == hash_code(old_password):
            user.password = hash_code(new_password)
            try:
                user.save()
                status = "changeSuccess"
            except Exception as e:
                print(e)
                status = "changeFail"
        else:
            status = "oldPasswordValidateError"
    result = {'status': status}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def generate_main_activity_plastics_data(request):
    gen_polymer_data = {}
    gen_polymer_name = models.MainAtGenName.objects.values()
    gen_polymer_data['gen_polymer'] = list(gen_polymer_name)

    special_polymer = models.ResearchSysu.objects.values(method=F("methods")).distinct()
    gen_polymer_data['special_polymer'] = list(special_polymer)
    return HttpResponse(json.dumps(gen_polymer_data, ensure_ascii=False))


def get_material_list_activity_data(request):
    polymer_category = request.POST.get('materialCategory')
    polymer_name = {}
    gen_polymer_name = models.MainAtGenName.objects.values()
    polymer_name['gen_polymer'] = list(gen_polymer_name)

    polymer_list = models.GeneralMaterial.objects\
        .values(method=F('material_name')).filter(material_categories=polymer_category).distinct()
    polymer_name['special_polymer'] = list(polymer_list)
    return HttpResponse(json.dumps(polymer_name, ensure_ascii=False))


def get_polymer_no_list_activity_data(request):
    polymer_category = request.POST.get('polymerName')
    polymer_name = {}
    gen_polymer_name = models.MainAtGenName.objects.values()
    polymer_name['gen_polymer'] = list(gen_polymer_name)

    polymer_list = models.GeneralMaterial.objects\
        .values(method=F('material_no')).filter(material_name=polymer_category).distinct()

    if len(polymer_list) == 0:
        polymer_list = models.ResearchSysu.objects\
            .values(method=F('component_num')).filter(methods=polymer_category).distinct()

    polymer_name['special_polymer'] = list(polymer_list)
    return HttpResponse(json.dumps(polymer_name, ensure_ascii=False))


def get_material_detail(request):
    material_no = request.POST.get('materialNo')
    if material_no == "" or "xx" in material_no:
        material_no = '1018LA'
    utTime = models.TestparaUt.objects.get(id=1).time.split(",")
    nirWaveLength = models.TestparaNir.objects.get(id=1).wave_length.split(",")
    ramanWaveNum = models.TestparaRaman.objects.get(id=1).wave_num.split(",")[77:-107]
    if "PPC" in material_no:
        sysuMaterial = models.ResearchSysu.objects.get(component_num=material_no)
        materialDetail = models.ResearchSysu.objects\
            .values("material_name", "processing_level", "feature", "application", "material_type",
                    "density", "melting_point", "melt_index", "glass_tra_temp", "tensile_modulus",
                    "bending_strength", "bending_modulus", "others", material_no=F("methods"),
                    manuOrComp=F("component"), distorion_temp=F("hdt"), tensile_strength=F("tys"),
                    elongation_at_break=F("tensile_fracture_break"), impact_strength=F("izod"))\
            .filter(component_num=material_no)
        if sysuMaterial.rheological_test is None:
            rlitems = []
            rlitemsfit = []
        else:
            rldata = json.loads(sysuMaterial.rheological_test)['niandu']
            rldatafit = json.loads(sysuMaterial.rheological_test)['niandu_fit']
            rlitems = list(rldata.items())
            rlitemsfit = list(rldatafit.items())

        materialDetailData = {'materialDetail': list(materialDetail),
                              'rlScatterData': rlitems,
                              'rlFitData': rlitemsfit,
                              'materialUt': list(zip(utTime, sysuMaterial.ut_data.split(","))),
                              'materialNir': list(zip(nirWaveLength, sysuMaterial.nir_data.split(","))),
                              'materialRaman': list(zip(ramanWaveNum, sysuMaterial.raman_data.split(",")[77:-107]))
                              }
    else:
        gmMaterial = models.GeneralMaterial.objects.get(material_no=material_no)
        gmId = gmMaterial.id
        materialDetail = models.GeneralMaterial.objects\
            .values("material_name", "material_no", "processing_level", "feature", "application",
                    "material_type", "density", "melting_point", "melt_index", "distorion_temp", "glass_tra_temp",
                    "tensile_strength", "tensile_modulus", "elongation_at_break", "bending_strength",
                    "bending_modulus", "impact_strength", "others",  manuOrComp=F("manufacturer"))\
            .filter(material_no=material_no)
        materialTestDetail = models.GmProcess.objects.get(gm_id=gmId)
        if gmMaterial.rheological_test is None:
            rlitems = []
            rlitemsfit = []
        else:
            rldata = json.loads(gmMaterial.rheological_test)['niandu']
            rldatafit = json.loads(gmMaterial.rheological_test)['niandu_fit']
            rlitems = list(rldata.items())
            rlitemsfit = list(rldatafit.items())

        materialDetailData = {'materialDetail': list(materialDetail),
                              'rlScatterData': rlitems,
                              'rlFitData': rlitemsfit,
                              'materialUt': list(zip(utTime, materialTestDetail.ut_data.split(","))),
                              'materialNir': list(zip(nirWaveLength, materialTestDetail.nir_data.split(","))),
                              'materialRaman': list(zip(ramanWaveNum, materialTestDetail.raman_data.split(",")[77:-107]))
                              }

    return HttpResponse(json.dumps(materialDetailData, ensure_ascii=False))


def search_material(request):
    search_name = request.POST.get("searchName")
    if search_name == "":
        status = "emptyError"
    try:
        get_material = models.GeneralMaterial.objects.get(material_no=search_name.upper())
        search_name = get_material.material_no
        status = "success"
    except ObjectDoesNotExist:
        try:
            get_material = models.ResearchSysu.objects.get(component_num=search_name.upper())
            search_name = get_material.component_num
            status = "success"
        except ObjectDoesNotExist:
            status = "emptyMaterial"
    result = {'status': status, 'materialName': search_name}
    return HttpResponse(json.dumps(result, ensure_ascii=False))


def gen_monitor_data(request):
    xIndex = request.POST.get("xIndex")
    xIndex = int(xIndex)
    if (xIndex % 100) == 0:
        xId = 1
    else:
        xId = xIndex
    onlineNir = models.NirMonitorTestData.objects.get(id=(xId % 100)).nir_data.split(",")
    responseNir = list(map(eval, onlineNir))
    predict_request = '{"inputs":%s}' % [responseNir]
    response = requests.post('http://localhost:8501/v1/models/composition_monitor:predict', data=predict_request)
    response.raise_for_status()
    prediction = response.json()['outputs'][0][0]
    nirWaveLength = models.TestparaNir.objects.get(id=1).wave_length.split(",")
    monitorData = {'nirMonitorData': list(zip(nirWaveLength, onlineNir)),
                   'compositionMonitorData': [str(xIndex), str(prediction)]}
    return HttpResponse(json.dumps(monitorData))
