# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class Cmp(models.Model):
    materialkind = models.CharField(max_length=256, blank=True, null=True)
    materialname = models.CharField(max_length=256, blank=True, null=True)
    dbtable = models.CharField(max_length=64, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'cmp'


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class GeneralMaterial(models.Model):
    material_categories = models.CharField(max_length=32, blank=True, null=True)
    scientific_name = models.CharField(max_length=32, blank=True, null=True)
    material_name = models.CharField(max_length=32, blank=True, null=True)
    material_no = models.CharField(max_length=32, blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    manufacturer = models.CharField(max_length=128, blank=True, null=True)
    processing_level = models.CharField(max_length=128, blank=True, null=True)
    feature = models.TextField(blank=True, null=True)
    application = models.CharField(max_length=256, blank=True, null=True)
    material_type = models.CharField(max_length=32, blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    melt_index = models.FloatField(blank=True, null=True)
    distorion_temp = models.FloatField(blank=True, null=True)
    glass_tra_temp = models.FloatField(blank=True, null=True)
    melting_point = models.FloatField(blank=True, null=True)
    tensile_strength = models.FloatField(blank=True, null=True)
    tensile_modulus = models.FloatField(blank=True, null=True)
    elongation_at_break = models.CharField(db_column='Elongation_at_Break', max_length=16, blank=True, null=True)  # Field name made lowercase.
    bending_strength = models.FloatField(blank=True, null=True)
    bending_modulus = models.FloatField(blank=True, null=True)
    impact_strength = models.CharField(max_length=32, blank=True, null=True)
    others = models.CharField(max_length=256, blank=True, null=True)
    rheological_test = models.TextField(blank=True, null=True)
    rheological_dp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'general_material'


class GmProcess(models.Model):
    id = models.IntegerField(primary_key=True)
    gm_id = models.IntegerField(blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    equipment = models.CharField(max_length=32, blank=True, null=True)
    rpm = models.CharField(max_length=16, blank=True, null=True)
    temp = models.CharField(max_length=16, blank=True, null=True)
    equip_param = models.IntegerField(blank=True, null=True)
    plc_param = models.IntegerField(blank=True, null=True)
    ut_data = models.TextField(blank=True, null=True)
    ut_para = models.IntegerField(blank=True, null=True)
    ut_dp = models.TextField(blank=True, null=True)
    nir_data = models.TextField(blank=True, null=True)
    nir_para = models.IntegerField(blank=True, null=True)
    nir_dp = models.TextField(blank=True, null=True)
    raman_data = models.TextField(blank=True, null=True)
    raman_para = models.IntegerField(blank=True, null=True)
    raman_dp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'gm_process'


class MainAtGenName(models.Model):
    id = models.IntegerField(primary_key=True)
    polymer_name = models.CharField(max_length=255, blank=True, null=True)
    kindnum = models.CharField(max_length=32, blank=True, null=True)
    poster = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'main_at_gen_name'


class ResearchSysu(models.Model):
    material_name = models.CharField(max_length=20, blank=True, null=True)
    methods = models.CharField(max_length=20, blank=True, null=True)
    component_num = models.CharField(max_length=256, blank=True, null=True)
    component = models.CharField(max_length=256, blank=True, null=True)
    test_id = models.IntegerField(blank=True, null=True)
    blend_eqm = models.CharField(max_length=20, blank=True, null=True)
    blend_eqm_rpm = models.CharField(max_length=20, blank=True, null=True)
    blend_eqm_temp = models.CharField(max_length=20, blank=True, null=True)
    processing_level = models.CharField(max_length=128, blank=True, null=True)
    feature = models.TextField(blank=True, null=True)
    application = models.CharField(max_length=256, blank=True, null=True)
    material_type = models.CharField(max_length=32, blank=True, null=True)
    density = models.FloatField(blank=True, null=True)
    melt_index = models.FloatField(blank=True, null=True)
    hdt = models.FloatField(blank=True, null=True)
    glass_tra_temp = models.FloatField(blank=True, null=True)
    melting_point = models.FloatField(blank=True, null=True)
    tys = models.FloatField(blank=True, null=True)
    tensile_modulus = models.FloatField(blank=True, null=True)
    tensile_fracture_break = models.CharField(max_length=16, blank=True, null=True)
    bending_strength = models.FloatField(blank=True, null=True)
    bending_modulus = models.FloatField(blank=True, null=True)
    izod = models.CharField(max_length=32, blank=True, null=True)
    others = models.CharField(max_length=256, blank=True, null=True)
    rheological_test = models.TextField(blank=True, null=True)
    rheological_dp = models.TextField(blank=True, null=True)
    test_eqm = models.CharField(max_length=20, blank=True, null=True)
    test_eqm_rpm = models.CharField(max_length=20, blank=True, null=True)
    test_eqm_temp = models.CharField(max_length=20, blank=True, null=True)
    test_eqm_param = models.IntegerField(blank=True, null=True)
    test_eqm_plc = models.IntegerField(blank=True, null=True)
    ut_para = models.IntegerField(blank=True, null=True)
    ut_data = models.TextField(blank=True, null=True)
    ut_dp = models.TextField(blank=True, null=True)
    nir_para = models.IntegerField(blank=True, null=True)
    nir_data = models.TextField(blank=True, null=True)
    nir_dp = models.TextField(blank=True, null=True)
    raman_para = models.IntegerField(blank=True, null=True)
    raman_data = models.TextField(blank=True, null=True)
    raman_dp = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'research_sysu'


class TestEqm(models.Model):
    id = models.IntegerField(primary_key=True)
    fir_hopper_temp = models.FloatField(blank=True, null=True)
    sec_hopper_temp = models.FloatField(blank=True, null=True)
    third_hopper_temp = models.FloatField(blank=True, null=True)
    die_head_temp = models.FloatField(blank=True, null=True)
    screw_speed = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'test_eqm'


class TestparaNir(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(blank=True, null=True)
    integration_time = models.IntegerField(blank=True, null=True)
    integration_count = models.IntegerField(blank=True, null=True)
    smooth_width = models.IntegerField(blank=True, null=True)
    dark_background = models.TextField(blank=True, null=True)
    bright_background = models.TextField(blank=True, null=True)
    wave_length = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testpara_nir'


class TestparaPlc(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(blank=True, null=True)
    fir_hopper_temp = models.FloatField(blank=True, null=True)
    sec_hopper_temp = models.FloatField(blank=True, null=True)
    third_hopper_temp = models.FloatField(blank=True, null=True)
    die_head_temp = models.FloatField(blank=True, null=True)
    screw_speed = models.FloatField(blank=True, null=True)
    screw_torque = models.FloatField(blank=True, null=True)
    melt_temp = models.FloatField(blank=True, null=True)
    melt_pressure = models.FloatField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testpara_plc'


class TestparaRaman(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(blank=True, null=True)
    laser_power = models.IntegerField(blank=True, null=True)
    integration_time = models.IntegerField(blank=True, null=True)
    integration_count = models.IntegerField(blank=True, null=True)
    smooth_width = models.IntegerField(blank=True, null=True)
    wave_num = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testpara_raman'


class TestparaUt(models.Model):
    id = models.IntegerField(primary_key=True)
    create_date = models.DateTimeField(blank=True, null=True)
    slit_distance = models.FloatField(blank=True, null=True)
    probe_frequency = models.FloatField(blank=True, null=True)
    sample_freq = models.FloatField(blank=True, null=True)
    time = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'testpara_ut'


class User(models.Model):
    username = models.CharField(primary_key=True, max_length=32)
    password = models.CharField(max_length=255)
    email = models.CharField(max_length=50, blank=True, null=True)
    phone = models.CharField(max_length=16, blank=True, null=True)
    institution = models.CharField(max_length=255, blank=True, null=True)
    privilege = models.CharField(max_length=255, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'user'
