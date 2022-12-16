# LicenseClassify

LicenseClassify is used to collect Open-Source license List, and identify license from license's content and license_name(Eg: maven's pom.xml's licenses tag name)

## parse pom.xml's <licenses><license><name>

Generally pom.xml's `<license><license><name></name></license></license>` is not normallized.

```python
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
```

output

```
Apache-2.0
LGPL-2.0
MIT
other
other
GPL-2.0
CC-BY-NC-3.0
LGPL-2.0
Apache-2.0
GPL-1.0
GPL-3.0
```

## parse License's content


## we support license_id list

please look at `SupportedLicense.txt`
