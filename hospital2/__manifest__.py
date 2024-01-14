{
    'name': 'hospital.pat',
    'category': 'Hospital',
    'data': [
        'security/ir.model.access.csv',
        'views/menu.xml',
        'views/patient_view.xml',
        'views/female_patient_view.xml',
        'views/appointment_view.xml',
        'data/sequence.xml',
        'views/inherit_sale.xml',
        'wizard/cancel_appointment_view.xml',
        'views/res_config_settings_views.xml',
        'views/operation_view.xml',


    ],
    'author': 'islam mohamed',
    'application': True,
    'sequence': -100,
    'depends': ['mail', 'sale'],

}
