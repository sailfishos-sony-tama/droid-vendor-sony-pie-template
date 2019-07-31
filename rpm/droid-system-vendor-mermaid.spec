%define multiple_rpms 1
%define rpm_device mermaid

%define variant -vendor

%define dsd_path ./

Requires(post): coreutils
Requires(post): libcap

%include droid-system-device/droid-system.inc

