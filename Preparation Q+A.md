# Linux Interview Questions

## Table of Contents
- [Attach and Detach Filesystem](#attach-and-detach-filesystem)
- [Print Last 15 Lines](#print-last-15-lines)
- [Enable Passwordless Authentication](#enable-passwordless-authentication)

---

## Attach and Detach Filesystem

**Q1: How do you attach and detach a filesystem in Linux?**  
You can use the `mount` and `umount` commands:

**Attach (Mount):**
```bash
mount /dev/sdX /mnt/mydir
```

# LINUX

### 1. How do you attach and detach a filesystem in Linux?    #attach-and-detach-filesystem

You can use the `mount` and `umount` commands:

**Attach (Mount):**
```bash
mount /dev/sdX /mnt/mydir
```

**Detach (Unmount):**
```bash
umount /mnt/mydir
```

*Example:*
```bash
mount /dev/sdb1 /mnt/backup
umount /mnt/backup
```

---

### 2. How do you print the last 15 lines of a file in Linux?

Use the `tail` command:
```bash
tail -n 15 filename.log
```

*Example:*
```bash
tail -n 15 /var/log/syslog
```

Alternate (also valid):
```bash
tail -15 filename.log
```

---

### 3. How do you enable passwordless SSH authentication between two servers?

**On Server A (source):**

1. Generate SSH key:
```bash
ssh-keygen -t rsa -b 4096
```

2. Copy the public key to Server B:
```bash
ssh-copy-id user@ServerB
```

**Alternative manual method:**
```bash
cat ~/.ssh/id_rsa.pub | ssh user@ServerB 'mkdir -p ~/.ssh && cat >> ~/.ssh/authorized_keys && chmod 600 ~/.ssh/authorized_keys'
```

> You'll be asked to enter the password once during this step.

**Test passwordless login:**
```bash
ssh user@ServerB
```

If it logs in without prompting for a password, it's working.

---
