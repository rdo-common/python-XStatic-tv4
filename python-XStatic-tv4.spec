%{?python_enable_dependency_generator}

%global pypi_name XStatic-tv4

Name:           python-%{pypi_name}
Version:        1.2.7.0
Release:        2%{?dist}
Summary:        tv4 JavaScript library (XStatic packaging standard)

License:        Public Domain
URL:            https://github.com/geraintluff/tv4/
Source0:        https://pypi.io/packages/source/X/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
Source1:        https://raw.githubusercontent.com/geraintluff/tv4/master/LICENSE.txt
BuildArch:      noarch

%description
tv4 - Tiny Validator (for v4 JSON Schema) JavaScript library packaged
for setuptools (easy_install) / pip.

Use json-schema draft v4 to validate simple values and complex objects
using a rich validation vocabulary.

%package -n xstatic-tv4-common
Summary: tv4 JavaScript library (XStatic packaging standard)

BuildRequires:  web-assets-devel
Requires:       web-assets-filesystem

%description -n xstatic-tv4-common
tv4 - Tiny Validator (for v4 JSON Schema) JavaScript library packaged
for setuptools (easy_install) / pip.

This package contains the javascript files.

%package -n python3-%{pypi_name}
Summary: tv4 JavaScript library (XStatic packaging standard)
%{?python_provide:%python_provide python3-%{pypi_name}}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools

Requires:       python3-XStatic
Requires:       xstatic-tv4-common = %{version}-%{release}

%description -n python3-%{pypi_name}
tv4 - Tiny Validator (for v4 JSON Schema) JavaScript library packaged
for setuptools (easy_install) / pip.

Use json-schema draft v4 to validate simple values and complex objects
using a rich validation vocabulary.

%prep
%setup -q -n %{pypi_name}-%{version}
cp %{SOURCE1} LICENSE

# patch to use webassets dir
sed -i "s|^BASE_DIR = .*|BASE_DIR = '%{_jsdir}/tv4'|" xstatic/pkg/tv4/__init__.py

%build
%{__python3} setup.py build

%install
%{__python3} setup.py install --skip-build --root %{buildroot}
# Move static files
mkdir -p %{buildroot}/%{_jsdir}/tv4
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/tv4/data/tv4.async-jquery.js %{buildroot}/%{_jsdir}/tv4
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/tv4/data/tv4.js %{buildroot}/%{_jsdir}/tv4
mv %{buildroot}/%{python3_sitelib}/xstatic/pkg/tv4/data/tv4.min.js %{buildroot}/%{_jsdir}/tv4

rmdir %{buildroot}/%{python3_sitelib}/xstatic/pkg/tv4/data/

%files -n xstatic-tv4-common
%doc README.txt
%license LICENSE
%{_jsdir}/tv4

%files -n python3-%{pypi_name}
%doc README.txt
%license LICENSE
%{python3_sitelib}/xstatic/pkg/tv4
%{python3_sitelib}/XStatic_tv4-%{version}-py?.?.egg-info
%{python3_sitelib}/XStatic_tv4-%{version}-py?.?-nspkg.pth

%changelog
* Fri Feb 21 2020 Yatin Karel <ykarel@redhat.com> - 1.2.7.0-2
- Drop python2 sub package

* Thu Sep 27 2018 Alfredo Moralejo <amoralej@redhat.com> - 1.2.7.0-1
- Rebuild in Fedora copr

* Fri Aug 5 2016 David Moreau Simard <dmsimard@redhat.com> - 1.2.7.0-0.1.pre_review
- First version
