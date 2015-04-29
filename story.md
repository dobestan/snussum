Story
---

* User can signup via mysnu account ( [USERNAME]@snu.ac.kr )
* User can login, logout

* User matches with another user without any condition

* User visits site. ( Main Page )
    * login required, but can access snussum analytics.
    * can NOT access matching, dating information.

* User logined.
    * Main Page
        * Personal Analytics
        * Personal Matching
        * Today Matching Summary

    * Today's Matching Page ( /today )
        * Today's Matching

    * Dashboard ( /ssum )
        * Matching History Summary

    * Matching Detail ( /ssum/<hash_id> )
        * Matching Information
        * Parnter Detail

* Verification Process
    * manage via user_profile property and decorator

    * verify/university, verify/snu
    * verify/profile

* Deploy Automation ( Staging Server, Production Server )
    * using Ansible.

    * Staging Server
        * using Vagrant
        * How to test SSL? ( Create a example SSL? )
        * should NOT upload to production s3 bucket ( use default S3 )

    * Production Server
        * using AWS EC2
        * real SSL
