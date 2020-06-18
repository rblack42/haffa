import os
import re
import sys
import datetime

version_re = re.compile("^version.*=.*\"(.*)\"$")
AUTHOR  = os.getenv('REALNAME')
YEAR = datetime.datetime.now().year

VERSION = "sphinxcontrib/pylit/meta.py"

class Versioning(object):

    def __init__(self, opt):
        """Initialize by reading existing strings from meta.py"""
        self.inc_opt = opt
        self.lines = []
        if os.path.isfile(VERSION):
            with open(VERSION) as fin:
                self.lines = fin.readlines()

    def _get_version_string(self):
        """Process lines looking for version string"""
        vstring = "0.0.0"
        if len(self.lines) == 0:
            self.lines.append("# Copyright %d %s\n" % (YEAR, AUTHOR))
            self.lines/append("\n")
            self.lines.append("version = %s\n" % vstring)

        # locate version string
        lc = 0
        for l in self.lines:
            m = version_re.match(l)
            if m:
                vstring = m.group(1)
                break
            else:
                lc+=1

        self.lc = lc
        self.vstring = vstring
        print("%s found on line %d" % (vstring, lc))

    def parse(self):
        self._get_version_string()
        major,minor,build = self.vstring.split('.')
        if self.inc_opt == "version":
            print("Current version:",self.vstring)
            sys.exit(0)

        if self.inc_opt == "major": major = str(int(major)+1)
        elif self.inc_opt == "minor": minor = str(int(minor)+1)
        else:
            if '-' in build:
                bval, tag = build.split('-')
                bval = int(bval) + 1
                build = str(bval) + '-' + tag
            else:
                bval = int(build)+1
                build = str(bval)
        self.vstring = major + '.' + minor + "." + build

    def update_version_string(self):
        self.lines[self.lc] = "version = \"%s\"" % self.vstring
        with open(VERSION, 'w') as fout:
            for l in self.lines:
                fout.write(l)

    def update_readme(self):
        """update README.rst"""
        fin = open("README.rst")
        lines = fin.readlines()
        fin.close()

        fout = open('README.rst','w')
        vline = lines[0]
        parts = vline.split()
        projname = parts[0]
        title = '%s (v%s)' % (projname, self.vstring)
        tline = '#' * len(title)
        fout.write('%s\n' % title)
        fout.write('%s\n' % tline)
        for l in lines[2:]:
            fout.write(l)
        fout.write("\n");
        fout.close()

def main(opt):
    v = Versioning(opt)
    v.parse()
    v.update_version_string()
    v.update_readme()

if __name__ == '__main__':
    try:
        inc_opt = sys.argv[1]
    except:
        inc_opt = "build"

    main(inc_opt)
