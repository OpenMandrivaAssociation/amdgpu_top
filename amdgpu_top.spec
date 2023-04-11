%define _empty_manifest_terminate_build 0
%define git 20230317
Name:           amdgpu_top
Version:        0.1.4
Release:        1
Summary:        tool to show AMDGPU usage
License:        MIT
URL:            https://github.com/Umio-Yasuno/amdgpu_top
# Until there are tagged releases, we use git.
#Source0:        https://github.com/Umio-Yasuno/amdgpu_top/archive/refs/heads/amdgpu_top-main.tar.gz
Source0:        https://github.com/Umio-Yasuno/amdgpu_top/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz
Source2:        cargo_config

ExclusiveArch:  %{rust_arches}
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libdrm)


%description
amdgpu_top is tool that show AMD GPU utilization, like umr or clbr/radeontop.
  
%prep
%autosetup -n %{name}-%{version} -p 1 -a 1
install -D -m 0644 %{SOURCE2} .cargo/config

%build
%cargo_build

%install
%cargo_install

install -Dm755 target/release/amdgpu_top %{buildroot}/usr/bin/amdgpu_top

%files
%{_bindir}/amdgpu_top
