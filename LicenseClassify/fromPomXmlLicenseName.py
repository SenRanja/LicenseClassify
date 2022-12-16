# encoding=utf-8

def licenseIdentifyFromPomName(n:str) -> str:
    # lower alphas for convinence
    if n == None:
        return 'other'
    n = n.lower()
    # [apache]
    if 'apache' in n and '2' in n:
        return "Apache-2.0"
    if 'apache' in n and '1.1' in n:
        return "Apache-1.1"
    if 'apache' in n and '1.0' in n:
        return "Apache-1.0"
    if 'apache' in n:
        return "Apache-1.0"
    if 'scala' in n:
        # its name is from url https://github.com/scala/scala/blob/2.13.x/LICENSE，declaired apache 2.0 in truth
        return "Apache-2.0"
    # [mit]
    if 'mit' in n.replace("limit", ""):
        return "MIT"
    # [bsd]
    if 'bsd' in n and '4' in n:
        return "BSD-4-Clause"
    if 'bsd' in n and '3' in n:
        return "BSD-3-Clause"
    if 'bsd' in n and '2' in n:
        return "BSD-2-Clause"
    if 'bsd' in n and '1' in n:
        return "BSD-1-Clause"
    if 'bsd' in n:
        return "BSD-Protection"
    # [lgpl]
    if 'lgpl' in n and '3.0' in n:
        return "LGPL-3.0"
    if 'lgpl' in n and '2.1' in n:
        return "LGPL-2.1"
    if 'lgpl' in n and '2.0' in n:
        return "LGPL-2.0"
    if 'lgpl' in n:
        return "LGPL-2.0"
    if 'lesser' in n and 'gnu' in n and '3' in n:
        return "LGPL-3.0"
    if 'lesser' in n and 'gnu' in n and '2.1' in n:
        return "LGPL-2.1"
    if 'lesser' in n and 'gnu' in n and '2.0' in n:
        return "LGPL-2.0"
    if 'lesser' in n and 'gnu' in n and '2' in n:
        return "LGPL-2.0"
    # [agpl]
    if 'agpl' in n and '3' in n:
        return "AGPL-3.0"
    if 'agpl' in n and '1' in n:
        return "AGPL-1.0"
    if 'agpl' in n:
        return "AGPL-1.0"
    # [gpl with exception]
    # # [gpl 3.0 with exception]
    if 'gpl' in n and 'gcc' in n and '3' in n:
        return "GPL-3.0-with-GCC-exception"
    if 'gpl' in n and 'autoconf' in n and '3' in n:
        return "GPL-3.0-with-autoconf-exception"
    if 'gpl' in n and 'source' in n and '3' in n:
        return "GPL-3.0-linking-source-exception"
    if 'gpl' in n and 'linking' in n and '3' in n:
        return "GPL-3.0-linking-exception"
    # # [gpl 2.0 with exception]
    if 'gpl' in n and 'classpath' in n:
        return "GPL-2.0-with-classpath-exception"
    if 'gpl' in n and 'GCC' in n:
        return "GPL-2.0-with-GCC-exception"
    if 'gpl' in n and 'font' in n:
        return "GPL-2.0-with-font-exception"
    if 'gpl' in n and 'bison' in n:
        return "GPL-2.0-with-bison-exception"
    if 'gpl' in n and 'autoconf' in n:
        return "GPL-2.0-with-autoconf-exception"
    # [gpl]
    if 'gpl' in n and '3' in n:
        return "GPL-3.0"
    if 'gnu' in n and '3' in n:
        return "GPL-3.0"
    if 'general' in n and 'public' in n and '3' in n:
        return "GPL-3.0"
    if 'gpl' in n and '2' in n:
        return "GPL-2.0"
    if 'gnu' in n and '2' in n:
        return "GPL-2.0"
    if 'general' in n and 'public' in n and '2' in n:
        return "GPL-2.0"
    if 'gpl' in n and '1' in n:
        return "GPL-1.0"
    if 'gnu' in n and '1' in n:
        return "GPL-1.0"
    if 'general' in n and 'public' in n and '1' in n:
        return "GPL-1.0"
    if 'gnu' in n:
        return "GPL-1.0"
    # [mpl]
    if ('mozilla' in n or 'mpl' in n) and '2' in n:
        return "MPL-2.0"
    if ('mozilla' in n or 'mpl' in n) and '1.1' in n:
        return "MPL-1.1"
    if ('mozilla' in n or 'mpl' in n) and '1' in n:
        return "MPL-1.0"
    if 'mozilla' in n or 'mpl' in n:
        return "MPL-1.0"
    # [apl]
    if 'apl' in n and '1' in n:
        return "APL-1.0"
    if 'apl' in n and '2' in n:
        return "APL-2.0"
    # [cddl]
    if 'cddl' in n and '1.1' in n:
        return "CDDL-1.1"
    if 'cddl' in n and '1.0' in n:
        return "CDDL-1.0"
    if 'cddl' in n:
        return "CDDL-1.0"
    # [mpl]
    if 'mpl' in n and '2' in n:
        return "MPL-2.0"
    if 'mpl' in n and '1.1' in n:
        return "MPL-1.1"
    if 'mpl' in n and '1.0' in n:
        return "MPL-1.0"
    if 'mpl' in n:
        return "MPL-1.0"
    # [cpl]
    if 'cpl' in n:
        return "CPL-1.0"
    if 'common' in n and 'public' in n:
        return "CPL-1.0"
    # [cpal]
    if 'cpal' in n:
        return "CPAL-1.0"
    # [cpol]
    if 'cpol' in n:
        return "CPOL-1.02"
    # [curl]
    if 'curl' in n:
        return "curl"
    # [json]
    if 'json' in n:
        return "JSON"
    # [CC-BY]
    # # [cc-by-nc-变种]
    # # [cc-by-nc-变种] 之 [CC-BY-NC-SA-]
    if 'cc' in n and 'by' in n and 'nc' in n and 'sa' in n and '4' in n:
        return "CC-BY-SA-4.0"
    if 'cc' in n and 'by' in n and 'nc' in n and 'sa' in n and '3' in n:
        return "CC-BY-NC-SA-3.0"
    if 'cc' in n and 'by' in n and 'nc' in n and 'sa' in n and '2.5' in n:
        return "CC-BY-NC-SA-2.5"
    if 'cc' in n and 'by' in n and 'nc' in n and 'sa' in n and '2' in n:
        return "CC-BY-NC-SA-2.0"
    if 'cc' in n and 'by' in n and 'nc' in n and 'sa' in n:
        return "CC-BY-SA-1.0"
    # # [cc-by-nc-变种] 之 [CC-BY-NC-ND-]
    if 'cc' in n and 'by' in n and 'nc' in n and 'nd' in n and '4' in n:
        return "CC-BY-NC-ND-4.0"
    if 'cc' in n and 'by' in n and 'nc' in n and 'nd' in n and '3' in n and 'igo' in n:
        return "CC-BY-NC-ND-3.0-IGO"
    if 'cc' in n and 'by' in n and 'nc' in n and 'nd' in n and '3' in n:
        return "CC-BY-NC-ND-3.0"
    if 'cc' in n and 'by' in n and 'nc' in n and 'nd' in n and '2.5' in n:
        return "CC-BY-NC-ND-2.5"
    if 'cc' in n and 'by' in n and 'nc' in n and 'nd' in n and '2' in n:
        return "CC-BY-NC-ND-2.0"
    if 'cc' in n and 'by' in n and 'nc' in n and 'nd' in n:
        return "CC-BY-NC-ND-1.0"
    # # [cc-by-nc]
    if 'creative' in n and 'attribution' in n and '4' in n:
        return "CC-BY-NC-4.0"
    if 'creative' in n and 'attribution' in n and '3' in n:
        return "CC-BY-NC-3.0"
    if 'creative' in n and 'attribution' in n and '2.5' in n:
        return "CC-BY-NC-2.5"
    if 'creative' in n and 'attribution' in n and '2.0' in n:
        return "CC-BY-NC-2.0"
    if 'creative' in n and 'attribution' in n and '1.0' in n:
        return "CC-BY-NC-1.0"
    if 'creative' in n and 'attribution' in n:
        return "CC-BY-NC-3.0"
    # # [cc-by-sa]
    if 'cc' in n and 'by' in n and 'sa' in n and '4' in n:
        return "CC-BY-SA-4.0"
    if 'cc' in n and 'by' in n and 'sa' in n and '3' in n and 'at' in n:
        return "CC-BY-SA-3.0-AT"
    if 'cc' in n and 'by' in n and 'sa' in n and '3' in n:
        return "CC-BY-SA-3.0"
    if 'cc' in n and 'by' in n and 'sa' in n and '2.5' in n:
        return "CC-BY-SA-2.5"
    if 'cc' in n and 'by' in n and 'sa' in n and '2.0' in n and 'uk' in n:
        return "CC-BY-SA-2.0-UK"
    if 'cc' in n and 'by' in n and 'sa' in n and '2' in n:
        return "CC-BY-SA-2.0"
    if 'cc' in n and 'by' in n and 'sa' in n and '1' in n:
        return "CC-BY-SA-1.0"
    if 'cc' in n and 'by' in n and 'sa' in n:
        return "CC-BY-SA-1.0"
    # # [cc-by-nd]
    if 'cc' in n and 'by' in n and 'nd' in n and '4' in n:
        return "CC-BY-ND-4.0"
    if 'cc' in n and 'by' in n and 'nd' in n and '3' in n:
        return "CC-BY-ND-3.0"
    if 'cc' in n and 'by' in n and 'nd' in n and '2.5' in n:
        return "CC-BY-ND-2.5"
    if 'cc' in n and 'by' in n and 'nd' in n and '2' in n:
        return "CC-BY-ND-2.0"
    if 'cc' in n and 'by' in n and 'nd' in n:
        return "CC-BY-ND-1.0"
    # # 简化的 [cc-by]
    if 'cc' in n and 'by' in n and '4' in n:
        return "CC-BY-4.0"
    if 'cc' in n and 'by' in n and '3' in n and 'us' in n:
        return "CC-BY-3.0-US"
    if 'cc' in n and 'by' in n and '3' in n and 'at' in n:
        return "CC-BY-3.0-AT"
    if 'cc' in n and 'by' in n and '3' in n:
        return "CC-BY-3.0"
    if 'cc' in n and 'by' in n and '2.5' in n:
        return "CC-BY-2.5"
    if 'cc' in n and 'by' in n and '2' in n:
        return "CC-BY-2.0"
    if 'cc' in n and 'by' in n:
        return "CC-BY-1.0"
    # [ISC]
    if 'open' in n and 'ie' in n:
        return "ISC"
    if 'isc' in n.replace("rdisc", ""):
        return "ISC"

    # [Now cann't identify, use 'other' instead of its raw name]
    return 'other'




