%define _empty_manifest_terminate_build 0

Name:           amdgpu_top
Version:        0.7.0
Release:        1
Summary:        tool to show AMDGPU usage
License:        MIT
URL:            https://github.com/Umio-Yasuno/amdgpu_top
Source0:        https://github.com/Umio-Yasuno/amdgpu_top/archive/refs/tags/v%{version}/%{name}-%{version}.tar.gz
Source1:        vendor.tar.xz

ExclusiveArch:  %{rust_arches}
BuildRequires:  rust-packaging
BuildRequires:  pkgconfig(ncurses)
BuildRequires:  pkgconfig(libdrm)


%description
amdgpu_top is tool that show AMD GPU utilization, like umr or clbr/radeontop.
  
%prep
%autosetup -n %{name}-%{version} -p 1 -a 1
%cargo_prep -v vendor
cat >>.cargo/config <<EOF

[source."git+https://github.com/Umio-Yasuno/libdrm-amdgpu-sys-rs"]
git = "https://github.com/Umio-Yasuno/libdrm-amdgpu-sys-rs"
replace-with = "vendored-sources"
EOF

%build
%cargo_build

%install
%cargo_install

install -Dm755 target/release/amdgpu_top %{buildroot}/usr/bin/amdgpu_top
install -Dm644 assets/amdgpu_top.desktop %{buildroot}/usr/share/applications/amdgpu_top.desktop

%files
%{_bindir}/amdgpu_top
%{_datadir}/applications/amdgpu_top.desktop
