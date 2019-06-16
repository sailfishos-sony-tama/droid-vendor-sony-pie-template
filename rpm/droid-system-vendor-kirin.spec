%define device kirin
%define rpm_device kirin

%define variant -vendor

%define dsd_path ./

Requires(post): coreutils
Requires(post): libcap

%include droid-system-device/droid-system.inc
