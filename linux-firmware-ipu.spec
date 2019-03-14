%define commit efd2c1cc375cff1c17b4259d99a7fee240c3b510
%define ipu4fw ipu4fw-1.0.0-*

Name:           linux-firmware-ipu
Version:        20180000
Release:        103
License:        GPL-1.0+ GPL-2.0+ MIT Distributable
Summary:        Firmware files used by the Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source:         http://localhost/cgit/projects/ipu4fw/snapshot/ipu4fw-1.0.0-2874.a95c4ef.tar.gz
Requires:       linux-firmware-doc

%description
This package includes firmware files required for some IPU devices to
operate.



%prep
%setup -q -n ipu4fw-1.0.0-2874.a95c4ef


%install
mkdir -p %{buildroot}/usr/lib/modules-load.d
mkdir -p %{buildroot}/usr/lib/modprobe.d
mkdir -p %{buildroot}/usr/lib/firmware
cp -a lib/firmware/ipu4_cpd_b0.bin %{buildroot}/usr/lib/firmware/ipu4_cpd_b0.bin
cp -a usr/lib/modules-load.d/ipu.conf %{buildroot}/usr/lib/modules-load.d/ipu.conf
cp -a usr/lib/modules-load.d/ipu_ici  %{buildroot}/usr/lib/modules-load.d/ipu_ici
cp -a usr/lib/modules-load.d/ipu_v4l2 %{buildroot}/usr/lib/modules-load.d/ipu_v4l2
cp -a usr/lib/modprobe.d/ipu_ops.conf %{buildroot}/usr/lib/modprobe.d/ipu_ops.conf


%files
%defattr(-,root,root,-)
# IPU4
/usr/lib/firmware/ipu4_cpd_b0.bin
/usr/lib/modules-load.d/ipu_ici
/usr/lib/modules-load.d/ipu_v4l2
/usr/lib/modprobe.d/ipu_ops.conf
/usr/lib/modules-load.d/ipu.conf

