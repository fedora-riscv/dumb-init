Name:           dumb-init
Version:        1.1.3
Release:        17%{?dist}
Summary:        Entry-point for containers that proxies signals

License:        MIT
URL:            https://github.com/Yelp/dumb-init
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# merged upstream patch https://github.com/Yelp/dumb-init/pull/116/
Patch0:         dumb-init.fix-test.patch

BuildRequires:  gcc, help2man

BuildRequires:  python2, python2-pytest, python2-mock

# /bin/xxd of vim-common of is needed for non-released versions
# BuildRequires:  vim-common

%description
dumb-init is a simple process supervisor and init system designed to run as
PID 1 inside minimal container environments (such as Docker).

* It can handle orphaned zombie processes.
* It can pass signals properly for simple containers.

%prep
%setup -q
%patch0 -p1

%build

# uncomment next line when building a non-released version
# make VERSION.h 

gcc -std=gnu99 %{optflags} -o %{name} dumb-init.c 
help2man --no-discard-stderr --include debian/help2man --no-info --name '%{summary}' ./%{name} > %{name}.1

%check
PATH=.:$PATH py.test tests/

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1



%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-17
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Thu Jul 12 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-16
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu Mar 15 2018 Iryna Shcherbina <ishcherb@redhat.com> - 1.1.3-15
- Update Python 2 dependency declarations to new packaging standards
  (See https://fedoraproject.org/wiki/FinalizingFedoraSwitchtoPython3)

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.1.3-11
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Wed Aug 31 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-10
- revert to python2

* Wed Aug 31 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-9
- support epel

* Fri Aug 26 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-8
- run tests

* Wed Aug 17 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-7
- let manpage automatically marked as document

* Wed Aug 17 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-6
- remove gzip after help2man
- add missing BuildRequire

* Wed Aug 17 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-4
- install 644 for manpage

* Wed Aug 17 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-3
- remove vim-common and use install

* Mon Aug 15 2016 Muayyad Alsadi <alsadi@gmail.com> - 1.1.3-2
- initial packaging
