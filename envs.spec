#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : envs
Version  : 1.3
Release  : 8
URL      : https://files.pythonhosted.org/packages/cf/b9/57bf61a3a788ead19fa5704dfb10ba5696276eb7f26a322d6fc9a1a9ef68/envs-1.3.tar.gz
Source0  : https://files.pythonhosted.org/packages/cf/b9/57bf61a3a788ead19fa5704dfb10ba5696276eb7f26a322d6fc9a1a9ef68/envs-1.3.tar.gz
Summary  : Easy access of environment variables from Python with support for strings, booleans, list, tuples, and dicts.
Group    : Development/Tools
License  : Apache-2.0 GPL-3.0
Requires: envs-bin = %{version}-%{release}
Requires: envs-license = %{version}-%{release}
Requires: envs-python = %{version}-%{release}
Requires: envs-python3 = %{version}-%{release}
Requires: click
BuildRequires : buildreq-distutils3

%description
# envs
Easy access of environment variables from Python with support for booleans, strings, lists, tuples, integers, floats, and dicts.

%package bin
Summary: bin components for the envs package.
Group: Binaries
Requires: envs-license = %{version}-%{release}

%description bin
bin components for the envs package.


%package license
Summary: license components for the envs package.
Group: Default

%description license
license components for the envs package.


%package python
Summary: python components for the envs package.
Group: Default
Requires: envs-python3 = %{version}-%{release}

%description python
python components for the envs package.


%package python3
Summary: python3 components for the envs package.
Group: Default
Requires: python3-core

%description python3
python3 components for the envs package.


%prep
%setup -q -n envs-1.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1549383517
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/envs
cp LICENSE %{buildroot}/usr/share/package-licenses/envs/LICENSE
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/envs

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/envs/LICENSE

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
