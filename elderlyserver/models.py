from django.db import models


class User(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='用户ID')  # 自增主键ID
    openid = models.CharField(max_length=128, unique=True, verbose_name='微信小程序用户唯一标识id')  # 唯一标识id
    name = models.CharField(max_length=45, blank=True, null=True, verbose_name='姓名')  # 用户姓名
    address = models.CharField(max_length=45, blank=True, null=True, verbose_name='地址')  # 详细地址信息
    phone_number = models.IntegerField(blank=True, null=True, verbose_name='电话号码')  # 联系电话
    mail = models.CharField(max_length=45, blank=True, null=True, verbose_name='电子邮箱')  # 电子邮箱地址
    gender = models.BooleanField(blank=True, null=True, verbose_name='性别')  # 性别（0女性/1男性）
    priority = models.IntegerField(blank=True, null=True, verbose_name='优先级')  # 用户优先级权重值
    age = models.IntegerField(blank=True, null=True, verbose_name='年龄')  # 用户年龄
    degree = models.IntegerField(blank=True, null=True, verbose_name='受教育程度')  # 教育程度级别
    interested = models.IntegerField(blank=True, null=True, verbose_name='兴趣领域')  # 兴趣领域编码
    have_information = models.BooleanField(blank=True, null=True, verbose_name='是否已经提供个人信息')  # 0没有提供/1已经提供

    class Meta:
        db_table = 'user'


class Work(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='工作ID')  # 自增主键ID
    des = models.CharField(max_length=45, blank=True, null=True, verbose_name='工作描述')  # 工作内容描述
    longitude = models.FloatField(blank=True, null=True, verbose_name='经度')  # 工作地点经度
    latitude = models.FloatField(blank=True, null=True, verbose_name='纬度')  # 工作地点纬度
    address = models.CharField(max_length=45, blank=True, null=True, verbose_name='工作地址')  # 工作地点文字描述
    hourly_pay = models.FloatField(blank=True, null=True, verbose_name='时薪')  # 每小时报酬金额
    is_long = models.BooleanField(blank=True, null=True, verbose_name='长期性')  # 是否长期工作（1长期/0短期）
    publish_time = models.DateTimeField(blank=True, null=True, verbose_name='发布时间')  # 工作发布时间
    type = models.IntegerField(blank=True, null=True, verbose_name='工作类型')  # 工作分类编号
    start_time = models.DateTimeField(blank=True, null=True, verbose_name='开始时间')  # 工作开始时间
    end_time = models.DateTimeField(blank=True, null=True, verbose_name='结束时间')  # 工作结束时间
    publisher_id_w = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='publisher_id_w', verbose_name='发布者ID')  # 工作发布者ID
    is_over = models.BooleanField(blank=True, null=True, verbose_name='这个工作是否已招够人或被取消')  # 工作状态（1结束/0已结束）

    class Meta:
        db_table = 'work'


class Volntary(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='志愿活动ID')  # 自增主键ID
    longitude = models.FloatField(blank=True, null=True, verbose_name='经度')  # 活动地点经度
    latitude = models.FloatField(blank=True, null=True, verbose_name='纬度')  # 活动地点纬度
    address = models.CharField(max_length=45, blank=True, null=True, verbose_name='活动地址')  # 活动地点文字描述
    publish_time = models.DateTimeField(blank=True, null=True, verbose_name='发布时间')  # 活动发布时间
    des = models.CharField(max_length=45, blank=True, null=True, verbose_name='活动描述')  # 活动内容描述
    start_time = models.DateTimeField(blank=True, null=True, verbose_name='开始时间')  # 活动开始时间
    end_time = models.DateTimeField(blank=True, null=True, verbose_name='结束时间')  # 活动结束时间
    time_money = models.FloatField(blank=True, null=True, verbose_name='时间价值')  # 志愿活动时间价值换算
    publisher_id_v = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='publisher_id_v', verbose_name='发布者ID')  # 活动发布者ID
    is_over = models.BooleanField(blank=True, null=True, verbose_name='这个志愿活动是否已招够人或被取消')  # 志愿活动状态（1结束/0已结束）

    class Meta:
        db_table = 'volntary'


class Activity(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='社交活动ID')  # 自增主键ID
    latitude = models.FloatField(blank=True, null=True, verbose_name='纬度')  # 活动地点纬度
    longitude = models.FloatField(blank=True, null=True, verbose_name='经度')  # 活动地点经度
    address = models.CharField(max_length=45, blank=True, null=True, verbose_name='活动地址')  # 活动地点文字描述
    publish_time = models.DateTimeField(blank=True, null=True, verbose_name='发布时间')  # 活动发布时间
    des = models.CharField(max_length=45, blank=True, null=True, verbose_name='活动描述')  # 活动内容描述
    start_time = models.DateTimeField(blank=True, null=True, verbose_name='开始时间')  # 活动开始时间
    end_time = models.DateTimeField(blank=True, null=True, verbose_name='结束时间')  # 活动结束时间
    time_money = models.FloatField(blank=True, null=True, verbose_name='时间价值')  # 参与活动需要的话费
    publisher_id_w = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='publisher_id_w', verbose_name='发布者ID')  # 活动发布者ID
    is_over = models.BooleanField(blank=True, null=True, verbose_name='这个工作是否已招够人或被取消')  # 工作状态（1结束/0已结束）

    class Meta:
        db_table = 'activity'


class ApplicationWork(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='工作申请ID')  # 自增主键ID
    des = models.CharField(max_length=45, blank=True, null=True, verbose_name='申请描述')  # 申请补充说明
    is_agree = models.BooleanField(blank=True, null=True, verbose_name='是否同意')  # 申请状态（1同意/0拒绝或待处理）
    applicant_id_w = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='applicant_id_w', verbose_name='申请人ID')  # 工作申请人ID
    work_id = models.ForeignKey(Work, on_delete=models.DO_NOTHING, db_column='work_id', verbose_name='工作ID')  # 申请的工作ID
    is_over = models.BooleanField(blank=True, null=True, verbose_name='申请是否结束')  # 活动状态（1结束/0已结束）
    worker_confirmed = models.BooleanField(default=False, verbose_name='工作者确认')
    employer_confirmed = models.BooleanField(default=False, verbose_name='发布者确认')

    class Meta:
        db_table = 'application_work'


class ApplicationVoluntary(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='志愿申请ID')  # 自增主键ID
    des = models.CharField(max_length=45, blank=True, null=True, verbose_name='申请描述')  # 申请补充说明
    application_id_v = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='application_id_v', verbose_name='申请人ID')  # 志愿申请人ID
    volntary_id = models.ForeignKey(Volntary, on_delete=models.DO_NOTHING, db_column='volntary_id', verbose_name='志愿活动ID')  # 申请的志愿活动ID
    is_agreed = models.BooleanField(blank=True, null=True, verbose_name='是否同意')  # 申请状态（1同意/0拒绝或待处理）
    is_over = models.BooleanField(blank=True, null=True, verbose_name='申请是否结束')  # 活动状态（1结束/0已结束）

    class Meta:
        db_table = 'application_voluntary'


class ApplicationActivity(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='活动申请ID')  # 自增主键ID
    des = models.CharField(max_length=45, blank=True, null=True, verbose_name='申请描述')  # 申请补充说明
    activity_id = models.ForeignKey(Activity, on_delete=models.DO_NOTHING, db_column='activity_id', verbose_name='活动ID')  # 申请的活动ID
    applicant_id_a = models.ForeignKey(User, on_delete=models.DO_NOTHING, db_column='applicant_id_a', verbose_name='申请人ID')  # 活动申请人ID
    is_agreed = models.BooleanField(blank=True, null=True, verbose_name='是否同意')  # 申请状态（1同意/0拒绝）
    is_over = models.BooleanField(blank=True, null=True, verbose_name='申请是否结束')  # 活动状态（1结束/0已结束）

    class Meta:
        db_table = 'application_activity'


class UserComment(models.Model):
    id = models.AutoField(primary_key=True, verbose_name='评论ID')  # 自增主键ID
    commenter = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_made', verbose_name='评论者ID')  # 发表评论的用户ID
    commented_user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments_received', verbose_name='被评论者ID')  # 被评论的用户ID
    rating = models.IntegerField(verbose_name='评论星级')  # 1-5星评分
    content = models.TextField(verbose_name='评论内容')  # 评论文本内容
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='创建时间')  # 评论创建时间

    class Meta:
        db_table = 'user_comment'