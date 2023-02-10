 
##### *Creating  disk* [You may want to do it later]

	gcloud compute disks create DISKNAME \
	--size 1000 \
	--zone europe-west4-a
---
##### *Creating TPU connected to disk* [You may not want to attach the disk here]

	 gcloud alpha compute tpus tpu-vm create TPUNAME \
	 --zone europe-west4-a \
	 --accelerator-type v3-8 \
	 --version v2-alpha \
	 --data-disk source=projects/[MYPROJECT]/zones/europe-west4-a/disks/DISKNAME 
---
##### *Creating Preemptible TPU [You may not want to attach the disk here]*

	gcloud compute tpus tpu-vm create TPUNAME \  
	--zone=europe-west4-a \ 
	--accelerator-type=v3-32 \ 
	--version=v2-alpha \  
	--preemptible  
---
##### *Connecting to TPU*

	gcloud alpha compute tpus tpu-vm ssh TPUNAME --zone europe-west4-a
---
##### *Attach/Detach Disk To TPU*

	gcloud alpha compute tpus tpu-vm [at/de]tach-disk TPUNAME \
	--disk=example-disk \ 
	--zone=europe-west4-a

---
##### *Disk Formattting*

- Find the disk using this command. Sth like sdb
	`sudo lsblk`

- Format the disk using this command. (Notice that /dev/sdb is the disk.)
	`sudo mkfs.ext4 -m 0 -E lazy_itable_init=0,lazy_journal_init=0,discard /dev/sdb`

- Mount the disk - and give everyone (Notice that /dev/sdb is the disk.)
	`sudo mkdir -p /mnt/disks/DISKNAME`
	`sudo mount -o discard,defaults /dev/sdb /mnt/disks/DISKNAME`
	`sudo chmod a+w /mnt/disks/DISKNAME`

- Configure automatic mount on restarts
	`sudo cp /etc/fstab /etc/fstab.backup`
	
- Find the uid of the disk - you need this value in the following steps
	`sudo blkid /dev/sdb`
- Add this to /etc/fstab with the correct uuid, sth like this using nano"
	`UUID=52af08e4-f249-4efa-9aa3-7c7a9fd560b0 /mnt/disks/flaxdisk ext4 discard,defaults,nofail 0 2`

---
#####  *Checking TPU-VMs status*
	gcloud compute tpus tpu-vm list --zone=europe-west4-a
---
