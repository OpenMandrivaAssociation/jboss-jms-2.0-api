%{?_javapackages_macros:%_javapackages_macros}
%global namedreltag .Alpha1
%global namedversion %{version}%{?namedreltag}

Name:             jboss-jms-2.0-api
Version:          1.0.0
Release:          0.3%{namedreltag}.1
Summary:          JBoss JMS API 2.0 Spec
Group:            Development/Java
License:          CDDL or GPLv2 with exceptions
Url:              https://www.jboss.org
Source0:          https://github.com/jboss/jboss-jms-api_spec/archive/jboss-jms-api_2.0_spec-%{namedversion}.tar.gz
Source1:          cddl.txt

BuildRequires:    jboss-parent
BuildRequires:    felix-osgi-foundation
BuildRequires:    felix-parent
BuildRequires:    maven-local

BuildArch:        noarch

%description
The Java Messaging Service 2.0 API classes

%package javadoc
Summary:          Javadocs for %{name}

%description javadoc
This package contains the API documentation for %{name}.

%prep
%setup -q -n jboss-jms-api_spec-jboss-jms-api_2.0_spec-%{namedversion}

cp %{SOURCE1} .

sed -i "s,59 Temple Place,51 Franklin Street,;s,Suite 330,Fifth Floor,;s,02111-1307,02110-1301," LICENSE

%build
%mvn_build

%install
%mvn_install

%files -f .mfiles
%dir %{_javadir}/%{name}
%doc LICENSE README cddl.txt

%files javadoc -f .mfiles-javadoc
%doc LICENSE README cddl.txt

%changelog
* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.3.Alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0.0-0.2.Alpha1
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Fri Jun 21 2013 Marek Goldmann <mgoldman@redhat.com> - 1.0.0-0.1.Alpha1
- Initial packaging


