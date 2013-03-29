Summary:	Ruby Database driver for MySQL
Name:		ruby-dbd-mysql
Version:	0.4.2
Release:	1
License:	Ruby License
Group:		Development/Libraries
Source0:	http://rubyforge.org/frs/download.php/46558/dbd-mysql-%{version}.tar.gz
# Source0-md5:	5008ae6b668bbccff3dd25fb03624233
URL:		http://rubyforge.org/projects/ruby-dbi/
BuildRequires:	ruby-modules
Requires:	ruby-mysql
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Ruby Database driver for MySQL.

%prep
%setup -q -n dbd-mysql-%{version}

%build
ruby setup.rb config \
	--rb-dir=%{ruby_rubylibdir} \
	--so-dir=%{ruby_archdir}
ruby setup.rb setup

%install
rm -rf $RPM_BUILD_ROOT
ruby setup.rb install \
	--prefix=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{ruby_rubylibdir}/dbd/mysql
%{ruby_rubylibdir}/dbd/Mysql.rb
