Name:           dumb-init
Version:        1.1.3
Release:        9%{?dist}
Summary:        Entry-point for containers that proxies signals

License:        MIT
URL:            https://github.com/Yelp/dumb-init
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz
# merged upstream patch https://github.com/Yelp/dumb-init/pull/116/
Patch0:         dumb-init.fix-test.patch

BuildRequires:  gcc, help2man

# EPEL does not have python3-pytest python3-mock
%if 0%{?rhel}
BuildRequires:  python34, python34-pytest python34-mock
%else
BuildRequires:  python3, python3-pytest python3-mock
%endif

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
PATH=.:$PATH py.test-3 tests/

%install
install -Dpm0755 %{name} %{buildroot}%{_bindir}/%{name}
install -Dpm0644 %{name}.1 %{buildroot}%{_mandir}/man1/%{name}.1



%files
%{_bindir}/%{name}
%{_mandir}/man1/%{name}.1*
%license LICENSE
%doc README.md

%changelog
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
