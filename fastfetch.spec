Name:           fastfetch
Version:        1.6.4
Release:        1%{?dist}
Summary:        Like neofetch, but much faster because written in c

License:        MIT
URL:            https://github.com/LinusDierheimer/fastfetch
Source0:        %{url}/archive/%{version}/%{name}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  pciutils-devel
BuildRequires:  vulkan-loader-devel
BuildRequires:  wayland-devel
BuildRequires:  libxcb-devel
BuildRequires:  libXrandr-devel
BuildRequires:  dconf-devel
BuildRequires:  dbus-devel
BuildRequires:  sqlite-devel
BuildRequires:  ImageMagick-devel
BuildRequires:  zlib-devel
BuildRequires:  libglvnd-devel
BuildRequires:  mesa-libOSMesa-devel
BuildRequires:  xfconf-devel
BuildRequires:  glib2-devel
BuildRequires:  ocl-icd-devel
%if 0%{?fedora} > 36
BuildRequires:  chafa-devel
%endif

Recommends:     pciutils
Recommends:     libxcb
Recommends:     libXrandr
Recommends:     dconf
Recommends:     sqlite
Recommends:     zlib
Recommends:     libglvnd-glx
Recommends:     ImageMagick
Recommends:     glib2
Recommends:     ocl-icd
%if 0%{?fedora} > 36
Recommends:     chafa
%endif

%description
fastfetch is a neofetch-like tool for fetching system information and
displaying them in a pretty way. It is written in c to achieve much better
performance, in return only Linux and Android are supported. It also uses
mechanisms like multithreading and caching to finish as fast as possible.


%package bash-completion
Summary: Bash completion files for %{name}
Requires: bash-completion
Requires: %{name} = %{version}-%{release}
BuildArch: noarch


%description bash-completion
%{summary}


%prep
%autosetup -p1


%build
%cmake -D BUILD_TESTS=ON
%cmake_build


%check
%ctest


%install
%cmake_install


%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/%{name}/
%{_bindir}/%{name}
%{_bindir}/flashfetch
%{_datadir}/%{name}/

%files bash-completion
%{_datadir}/bash-completion/completions/%{name}

%changelog
* Tue Aug 16 2022 Jonathan Wright <jonathan@almalinux.org> - 1.6.4-1
- Initial package build
- khbz#2118887
