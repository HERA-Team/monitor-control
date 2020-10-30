from __future__ import print_function
from datetime import datetime
import os
import warnings


class HostsEthers:
    def __init__(self, filename):
        self.filename = filename
        with open(filename, 'r') as fp:
            self.file_contents_by_line = fp.read().splitlines()
        self.original_contents_by_line = []
        for line in self.file_contents_by_line:
            self.original_contents_by_line.append(line)

    def rewrite_file(self):
        """
        Writes the contents of list "file_contents_by_line" to the filename, showing
        differences.  It does not handle removed lines gracefully at all (but no
        method currently does that.)
        """
        if len(self.file_contents_by_line) == 0:
            print("{} in memory to rewrite is empty - skipping"
                  .format(self.filename))
            return
        differences = []
        for iline, line in enumerate(self.file_contents_by_line):
            try:
                if self.original_contents_by_line[iline] != line:
                    differences.append((self.original_contents_by_line[iline], line))
            except IndexError:
                differences.append(('[Added] ', line))

        if len(differences) == 0:
            print("No changes to {}.".format(self.filename))
            return
        print("Differences are:")
        print("{:40s}     {}".format("Original", "New"))
        print("{}     {}".format(40*'-', 40*'-'))
        for diff in differences:
            print("{:40s}     {}".format(diff[0], diff[1]))

        with open(self.filename, 'w') as fp:
            for line in self.file_contents_by_line:
                print("{}".format(line), file=fp)

    def update_id(self, id, val):
        """
        Take an id (mac or ip) and update its value or write new line if id not
        present.  This updates the attributes by_id and by_alias, as well as the
        file contents.

        Parameters
        ----------
        id : str
            Mac or ip id
        val : str
            Value to be associated with that id.
        """
        if id in self.by_id.keys():
            print("Updating {}:   <{}>   -->  <{}>".format(id, self.by_id[id], val))
        else:
            print("Adding:  {}  {}".format(id, val))
        self.by_id[id] = val
        for d in val.split():
            self.by_alias[d] = id
        new_contents = []
        for line in self.file_contents_by_line:
            data = line.split()
            if data == id:
                new_contents.append("{}\t{}".format(id, val))
            else:
                new_contents.append(line)
        self.file_contents_by_line = new_contents

    def archive_file(self, path_to_archive='.', date_tag="%y%m%d-%H%M"):
        """
        Will copy the original file to new.

        Parameters
        ----------
        path_to_archive : str
            Path to which to write the new file.
        date_tag : str or bool(False)
            if not bool(False), will use that datetime format to tag the file.
        """
        fn = os.path.basename(self.filename)
        if date_tag:
            fn = "{}_{}".format(fn, datetime.strftime(datetime.now()))
        os.copy(self.filename, os.path.join(path_to_archive, fn))

    def parse_file(self):
        """
        Read in the hosts or ethers file and send an e-mail on error.

        Attributes
        ----------
        by_id : dict
            entries with id (mac or ip) as key, listing all aliases
        by_alias : dict
            keyed on the aliases, value is the mac/ip
        """
        self.by_id = {}
        self.by_alias = {}
        for line in self.file_contents_by_line:
            if len(line) < 10 or line[0] == '#':
                continue
            data = line.split()
            if data[0] in self.by_id.keys():
                msg = '{} is duplicated in {} file on {}'.format(data[0], self.filename)
                warnings.warn(msg)
            self.by_id[data[0]] = data[1:]
            for d in data[1:]:
                if d in self.by_id.keys():
                    msg = '{} is duplicated in {} file on {}'.format(data[0], self.filename)
                    warnings.warn(msg)
                self.by_alias[d] = data[0]