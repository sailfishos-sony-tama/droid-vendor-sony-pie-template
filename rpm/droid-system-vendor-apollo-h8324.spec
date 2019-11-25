%define __find_provides %{nil}
%define __find_requires %{nil}
%define __strip /bin/true
%define __provides_exclude_from ^/system/.*$
%define __requires_exclude ^.*$
%global debug_package %{nil}

%define habuild_device apollo
%define device h8324

Name:          droid-system-vendor-%{habuild_device}-%{device}
Summary:       Built from source /vendor for Droid HAL adaptations
Version:       0.0.1
Release:       1
Group:         System
License:       Proprietary
Requires:      droid-system-vendor-%{habuild_device}
Source0:       %{name}-%{version}.tgz
Source1:       droid-system-vendor-%{habuild_device}-rpmlintrc
URL:           https://github.com/mer-hybris/droid-vendor-sony-pie-template

%description
%{summary}

%prep
%setup -q -n %{name}-%{version}

# This section is empty by purpose
%build

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/vendor
mkdir -p $RPM_BUILD_ROOT/vendor/etc/vintf
cp %{device}/vendor/build.prop $RPM_BUILD_ROOT/vendor/build.prop
cp %{device}/vendor/etc/vintf/manifest.xml $RPM_BUILD_ROOT/vendor/etc/vintf/manifest.xml

%files
%defattr(-,root,root,-)
/vendor/build.prop
/vendor/etc/vintf/manifest.xml
