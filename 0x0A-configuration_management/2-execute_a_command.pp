# Filename: 2-execute_a_command.pp

exec { 'killmenow':
  command  => 'pkill -f killmenow',
  provider => 'shell'
}
