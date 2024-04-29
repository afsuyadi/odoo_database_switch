import paramiko
from odoo import models, api, fields, _

class DatabaseSwitch(models.TransientModel):
    # _name = 'switch'
    _inherit = 'res.config.settings'
    
    is_database_switched = fields.Boolean('Database Switch', default=False)

    @api.constrains('is_database_switched')
    def _check_database_switch(self):
        pass
    
    @api.model
    def switch_database_and_access_config(self):
        # Connect to SSH server
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect('your_ssh_host', username='afsuyadi', password='afsuyadi2023')

        # Command to read config file
        ssh_stdin, ssh_stdout, ssh_stderr = ssh.exec_command('cat /path/to/config/file')

        # Read config file content
        config_content = ssh_stdout.read().decode('utf-8')

        # Parse config file content (example: if config file is in JSON format)
        import json
        config_data = json.loads(config_content)

        # Close SSH connection
        ssh.close()

        # Switch database based on config data
        db_name = config_data.get('database_name')
        if db_name:
            self.env.cr.close()
            self.env.cr.dbname = db_name
            self.env.cr.open()

        # Now you can perform operations on the switched database
        # Example: 
        # self.env['your.model'].search([])
        
        self.is_database_switched = True

        # return True