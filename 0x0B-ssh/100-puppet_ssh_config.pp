
# Connecting to server using puppet

file_line { 'TurnOffPasswordAuthy':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => ' PasswordAuthentication no';
  }

file_line { 'DeclareIdentityFile':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => ' IdentityFile ~/.ssh/school';
  }