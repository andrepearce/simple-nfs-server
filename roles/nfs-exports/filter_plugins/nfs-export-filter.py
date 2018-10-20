def nfs_export(export):
  '''
  Format a given dictionary as a string for an NFS export.
  Refer to https://linux.die.net/man/5/exports.
  '''

  clients = []
  for client in export['clients']:
    option_delimeter = ","
    clients.append(client['address'] + "(" + option_delimeter.join(client['options']) + ")")

  client_delimeter = " "

  return export['directory'] + "\t" + client_delimeter.join(clients)


class FilterModule(object):
  '''
  Custom Jinja2 filters for formating a string as an NFS export.
  '''

  def filters(self):
    return {
      'nfs_export': nfs_export
    }