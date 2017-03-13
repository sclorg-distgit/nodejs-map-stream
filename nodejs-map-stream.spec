%{?scl:%scl_package nodejs-%{module_name}}
%{!?scl:%global pkg_name %{name}}
%{?nodejs_find_provides_and_requires}

# Disabled as BR: for tests are not in fedora
%global enable_tests 0

%global module_name map-stream

Name:           %{?scl_prefix}nodejs-%{module_name}
Version:        0.1.0
Release:        6%{?dist}
Summary:        Construct pipes of streams of events

License:        MIT
URL:            http://github.com/dominictarr/map-stream
Source0:        http://registry.npmjs.org/%{module_name}/-/%{module_name}-%{version}.tgz
BuildArch:      noarch
ExclusiveArch:  %{nodejs_arches} noarch

BuildRequires:  %{?scl_prefix}nodejs-devel

%if 0%{?enable_tests}
BuildRequires:  %{?scl_prefix}npm(asynct)
BuildRequires:  %{?scl_prefix}npm(it-is)
BuildRequires:  %{?scl_prefix}npm(ubelt)
BuildRequires:  %{?scl_prefix}npm(stream-spec)
BuildRequires:  %{?scl_prefix}npm(event-stream)
BuildRequires:  %{?scl_prefix}npm(from)
%endif

%description
%{summary}.

%prep
%setup -q -n package
rm -rf node_modules

%build
# nothing to build

%install
mkdir -p %{buildroot}%{nodejs_sitelib}/%{module_name}
cp -pr package.json index.js %{buildroot}%{nodejs_sitelib}/%{module_name}

%nodejs_symlink_deps

%if 0%{?enable_tests}

%check
%nodejs_symlink_deps --check
asynct test
%endif

%files
%doc readme.markdown LICENCE examples
%{nodejs_sitelib}/%{module_name}

%changelog
* Tue Feb 16 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.0-6
- Use macro in -runtime dependency

* Sun Feb 14 2016 Zuzana Svetlikova <zsvetlik@redhat.com> - 0.1.0-5
- Rebuilt with updated metapackage

* Thu Jan 14 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.0-4
- Enable find provides and requires macro

* Thu Jan 07 2016 Tomas Hrcka <thrcka@redhat.com> - 0.1.0-3
- Enable scl macros

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Thu Dec 25 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.1.0-1
- Update to 0.1.0

* Tue Dec 09 2014 Parag Nemade <pnemade AT redhat DOT com> - 0.0.5-1
- Initial packaging
