# Created by pyp2rpm-3.3.4
%global oname NonMouse
%global pypi_name nonmouse

%define Summary Webcam-based virtual gesture mouse that is easy to use with hands
%define Summary_hu Webkamera alapú virtuális egér ami kézmozgással használható

Name:           %{pypi_name}
Version:        2.7.0
Release:        %mkrel 1
Summary:        %Summary
Summary(hu):    %Summary_hu
Group:          Development/Python
License:        Apache-2.0
URL:            https://github.com/takeyamayuki/NonMouse
Vendor:		blackPanther Europe
Packager:	Charles K Barcza <kbarcza@blackpanther.hu>
Source0:        https://files.pythonhosted.org/packages/source/n/%{pypi_name}/%{pypi_name}-%{version}.tar.gz
# icon created by Charles K Barcza
Source1:	%name.png
Patch0:		%name-wont-start-fix.patch
BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3dist(setuptools)

%{?python_provide:%python_provide python3-%{pypi_name}}

Requires:       python3dist(absl-py)
Requires:       python3dist(altgraph)
Requires:       python3dist(attrs)
Requires:       python3dist(cycler)
Requires:       python3dist(fonttools)
Requires:       python3dist(keyboard)
Requires:       python3dist(kiwisolver)
Requires:       python3dist(macholib)
Requires:       python3dist(matplotlib)
Requires:       python3dist(mediapipe)
Requires:       python3dist(numpy)
Requires:       python3dist(opencv-contrib-python)
Requires:       python3dist(packaging)
Requires:       python3dist(pillow)
Requires:       python3dist(protobuf)
Requires:       python3dist(pynput)
Requires:       python3dist(pyparsing)
Requires:       python3dist(python-dateutil)
Requires:       python3dist(six)

%description
Webcam-based virtual gesture mouse that is easy to use with hands on the desk


%prep
%autosetup -n %{pypi_name}-%{version} -p1
# Remove bundled egg-info
rm -rf %{pypi_name}.egg-info
echo > requirements.txt

%build
%py3_build

%install
%py3_install

%define nameicon %SOURCE1
mkdir -p -m755 %{buildroot}{%_liconsdir,%_iconsdir,%_miconsdir}
convert -scale 48x48 %{nameicon} %{buildroot}/%{_liconsdir}/%{name}.png
convert -scale 32x32 %{nameicon} %{buildroot}/%{_iconsdir}/%{name}.png
convert -scale 16x16 %{nameicon} %{buildroot}/%{_miconsdir}/%{name}.png

rm -rf %{buildroot}%{_datadir}/applications
mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/blackPanther-%{name}.desktop <<EOF
[Desktop Entry]
Name=%oname
Comment=%Summary
Comment[hu]=%Summary_hu
GenericName=%Summary
GenericName[hu]=%Summary_hu
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
StartupNotify=true
Categories=Utility;Accessibility;
Keywords=handmouse;no mouse;
Keywords[hu]=kéziegér;kézegér;nincs egér;
EOF


%files
%doc README.md
%_bindir/%name
%{python3_sitelib}/%{pypi_name}
%{python3_sitelib}/%{pypi_name}-%{version}-py%{python3_version}.egg-info
%{_datadir}/applications/blackPanther-%{name}.desktop
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_miconsdir}/%{name}.png

%changelog
* Fri Sep 15 2023 Charles K Barcza  <kbarcza@blackpanther.hu> - 2.7.0-1bP
- Initial for blackPanther OS generated with Pyp2Rpm
--------------------------------------------------------------------
