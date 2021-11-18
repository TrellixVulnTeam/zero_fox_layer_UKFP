# 0_fox_layer

## this app will provide an abstract layer between the network engineer and any configurable network device for any manufacture
## the abstract layer will consist of:
  * python flask app
    * api endpoints
    * endpoint function
  * ansible server
## the network engineer will:
  * consume that available endpoint of the product
    * the appropriate ansible module to be used will depend of the api that is consumed
  * supply the configuration properties to be configured on that device
    * a format to write the configuration properties based on the endpoint used will be provided to the using using an "endpoint info" api
    * example:
      * **task**: configure OSPF on nexus device
      * **configuration endpoint**: https://[server_ip_address]/ospf_nexus/
      * **endpoint info url**: https://[server_ip_address]/ospf_nexus/info/
        * this will return a format/template that must be used to configure OSPF on a nexus device
## the parts of the abstract layer will do the following upon receiving the request from the network engineer
 * **python flask app**: 
   * this will hold the **api endpoint** and its respective **endpoint function** tied to that endpoint
     * **api endpoint**: the appropriate endpoint consumed will trigger its respective endpoint function to perform the configuration on the device via ansible
     * **endpoint function**:
       * the function portion of the python flask app will do the following:
         * use the appropriate **ansible module** to create the **ansible playbook** to perform the configuation on the device
         * create the ansible playbook based on the configuration properties that the network engineer provided in the request
         * will execute the **ansible command** to use the playbook created to configure the device based on the configuration properties provided by the network engineer in the request
     * example:
       * **task**: configure OSPF on nexus device
       * **api endpoint**: https://[server_ip_address]/ospf_nexus/
       * **endpoint function**: 
         * **ansible module configured to be used in this endpoint function**: nxos_ospf
         * **ansible playbook used**: this will be create by the function with the configuration properties provided by the network engineer in the request
         * **execute the ansible cli command**:
           * ```ansible-playbook [playbook_filename] -i [inventory filename]```
      
   * the function will create the ansible playbook based on the configuration properties that the network engineer provided in the request
