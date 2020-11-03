Name:           linux-firmware-ipu
Version:        19ww39
Release:        105
License:        GPL-1.0+ GPL-2.0+ MIT Distributable
Summary:        Firmware files used by the Linux kernel
Url:            http://www.kernel.org/
Group:          kernel
Source:         http://localhost/cgit/projects/ipu4fw/snapshot/ipu4fw-1.0.0-4016.2bf1545.tar.xz
Requires:       linux-firmware-doc

%description
This package includes firmware files required for some IPU devices to
operate.


%prep
%setup -q -n ipu4fw-1.0.0-4016.2bf1545


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
/usr/lib/firmware/ipu4_cpd_b0.bin
/usr/lib/modules-load.d/ipu_ici
/usr/lib/modules-load.d/ipu_v4l2
/usr/lib/modprobe.d/ipu_ops.conf
/usr/lib/modules-load.d/ipu.conf
