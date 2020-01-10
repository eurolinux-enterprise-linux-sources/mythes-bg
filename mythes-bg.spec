Name: mythes-bg
Summary: Bulgarian thesaurus
Version: 4.3
Release: 5%{?dist}
Source: http://downloads.sourceforge.net/sourceforge/bgoffice/OOo-thes-bg-%{version}.zip
Requires: mythes
Group: Applications/Text
URL: http://bgoffice.sourceforge.net/
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
BuildRequires: unzip
License: GPLv2+ or LGPLv2+ or MPLv1.1
BuildArch: noarch

%description
Bulgarian thesaurus.

%prep
%setup -q -n OOo-thes-bg-%{version}

%build
for i in ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian; do
  if ! iconv -f utf-8 -t utf-8 -o /dev/null $i > /dev/null 2>&1; then
    iconv -f ISO-8859-2 -t UTF-8 $i > $i.new
    touch -r $i $i.new
    mv -f $i.new $i
  fi
  tr -d '\r' < $i > $i.new
  touch -r $i $i.new
  mv -f $i.new $i
done
echo "UTF-8" > th_bg_BG.dat.new
tail -n +2 th_bg_BG.dat | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> th_bg_BG.dat.new
mv th_bg_BG.dat.new th_bg_BG.dat
echo "UTF-8" > th_bg_BG.idx.new
tail -n +2 th_bg_BG.idx | iconv -f WINDOWS-1251 -t UTF-8 | tr -d '\r' >> th_bg_BG.idx.new
mv th_bg_BG.idx.new th_bg_BG.idx

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/mythes
cp -p th_bg_BG.dat $RPM_BUILD_ROOT/%{_datadir}/mythes/th_bg_BG_v2.dat
cp -p th_bg_BG.idx $RPM_BUILD_ROOT/%{_datadir}/mythes/th_bg_BG_v2.idx

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%doc ChangeLog Copyright GPL-2.0.txt LGPL-2.1.txt MPL-1.1.txt README.bulgarian
%{_datadir}/mythes/*

%changelog
* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Fri Jul 20 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.3-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jun 18 2010 Caolán McNamara <caolanm@redhat.com> - 4.3-1
- latest version

* Sat Apr 17 2010 Caolán McNamara <caolanm@redhat.com> - 4.2-1
- latest version

* Sat Apr 03 2010 Caolán McNamara <caolanm@redhat.com> - 4.1-4
- mythes now owns /usr/share/mythes

* Sat Jul 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Wed Feb 25 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Feb 03 2009 Caolán McNamara <caolanm@redhat.com> - 4.1-1
- initial version
