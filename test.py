from LicenseClassify import licenseIdentifyFromPomName

fake_license_name = [
    'Apache Software License version 2.0',
    'GNU General Lesser Public License (LGPL)',
    '\n\t\t\t\tMIT License\n\t\t\t',
    'Applitools License',
    'AppNeta Java Agent License',
    'GPL 2.0',
    'Creative Commons Attribution-ShareAlike ',
    'GLGPL v3',
    'Apache-2',
    'GNU LESSER GENERAL PUBLIC LICENSE\n      ',
    'GNU GPL v3',
]

for i in fake_license_name:
    print(licenseIdentifyFromPomName(i))