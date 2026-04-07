# -*- coding: utf-8 -*-
{
    'name': "Mommy Base",

    'summary': """
        Basic feature powered by Odoomommy.com
    """,

    'description': """
        1. 支持指定计算字段分组汇总
        2. 快速编辑功能可控
        3. 控制个人编辑区域显示效果
        4. 设置系统标题
        5. 封装统一提示框和统一确认框
        6. 表单设置每页条目数量
        7. 集成模型字段跟踪功能
        8. 集成快速设置单据号码方法
        9. 设置字段标签颜色
        10. 报表支持打印前校验
        11. 新增表单动作视图快速获取方法的方法
        12. 添加字段唯一性校验，支持定制提示文字
        13. 登录页面屏蔽数据库管理链接&Powered by Odoo
    """,

    'author': "Kevin Kong",
    'website': "http://www.odoomommy.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'basic',
    'version': '16.4.4',

    # any module necessary for this one to work correctly
    'depends': ['mail'],

    # always loaded
    'data': [
        'security/data.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/settings.xml',
        'views/pops.xml',
        'views/ir.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    "price":"200",
    "currency":"USD",
    "assets": {
        "web.assets_backend":[
            "mommy_base/static/src/js/mommy.js",
            "mommy_base/static/src/js/form/*",
            "mommy_base/static/src/js/fields/*",
            "mommy_base/static/src/js/models/*",
        ],
        "web.assets_qweb":[
            "mommy_base/static/srx/xml/*"
        ]
    }
}
