%define oname maruku

Name:       rubygem-%{oname}
Version:    0.5.9
Release:    2
Summary:    Maruku is a Markdown-superset interpreter written in Ruby
Group:      Development/Ruby
License:    GPLv2+ or Ruby
URL:        http://maruku.rubyforge.org
Source0:    %{oname}-%{version}.gem
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root
Requires:   rubygems
BuildRequires: rubygems
BuildArch:  noarch
Provides:   rubygem(%{oname}) = %{version}

%description
Maruku is a Markdown interpreter in Ruby. It features native export to HTML
and PDF (via Latex). The output is really beautiful!


%prep

%build

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}%{ruby_gemdir}
gem install --local --install-dir %{buildroot}%{ruby_gemdir} \
            --force --rdoc %{SOURCE0}
mkdir -p %{buildroot}/%{_bindir}
mv %{buildroot}%{ruby_gemdir}/bin/* %{buildroot}/%{_bindir}
rmdir %{buildroot}%{ruby_gemdir}/bin
find %{buildroot}%{ruby_gemdir}/gems/%{oname}-%{version}/bin -type f | xargs chmod a+x

%clean
rm -rf %{buildroot}

%files
%defattr(-, root, root, -)
%{_bindir}/maruku
%{_bindir}/marutex
%dir %{ruby_gemdir}/gems/%{oname}-%{version}/
%{ruby_gemdir}/gems/%{oname}-%{version}/bin/
%{ruby_gemdir}/gems/%{oname}-%{version}/lib/
%{ruby_gemdir}/gems/%{oname}-%{version}/tests/
%{ruby_gemdir}/gems/%{oname}-%{version}/maruku_gem.rb
%{ruby_gemdir}/gems/%{oname}-%{version}/*.sh
%doc %{ruby_gemdir}/doc/%{oname}-%{version}
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/Rakefile
%doc %{ruby_gemdir}/gems/%{oname}-%{version}/docs
%{ruby_gemdir}/cache/%{oname}-%{version}.gem
%{ruby_gemdir}/specifications/%{oname}-%{version}.gemspec


%changelog
* Sun Dec 19 2010 Rémy Clouard <shikamaru@mandriva.org> 0.5.9-1mdv2011.0
+ Revision: 623121
- import rubygem-maruku

