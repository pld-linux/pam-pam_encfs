Summary:	pam_encfs is a module to auto mount encfs dir on login
Name:		pam-pam_encfs
Version:	0.1
Release:	0.1
Epoch:		0
License:	GPL
Group:		Applications
Source0:	http://hollowtube.mine.nu/releases/pam_encfs/pam_encfs-0.1.tar.gz
# Source0-md5:	b1896bb8687dc68b5b7c9c1d70c2928e
URL:		http://hollowtube.mine.nu/wiki/index.php/PAM/PamEncfs
BuildRequires:	pam-devel
Requires:	encfs >= 1.2.1-4
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libdir	/%{_lib}

%description
pam_encfs is a pam module to auto mount encfs dir on login.

%prep
%setup -q -n pam_encfs-%{version}

%build
%{__make} \
	CFLAGS="%{rpmcflags} -fPIC -c -Wall -Wformat-security" \
	LDFLAGS="%{rpmldflags} -x --shared"

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_sysconfdir}
%{__make} install \
	PAM_LIB_DIR='$(DESTDIR)%{_libdir}/security' \
	DESTDIR=$RPM_BUILD_ROOT

install pam_encfs.conf $RPM_BUILD_ROOT%{_sysconfdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README
%config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/*
%attr(755,root,root) %{_libdir}/security/pam_encfs.so
