import os
import sipconfig

#The name of the directory where sip files reside
sip_directory="sip"

#The name of the directory where sip generated files will be placed
code_directory = "build"

# The name of the SIP build file generated by SIP and used by the build
# system.
build_file = "PyIndimod.sbf"
if code_directory != "":
    sip_build_file=code_directory+os.sep+build_file

# Get the SIP configuration information.
config = sipconfig.Configuration()

# Run SIP to generate the code.
os.system(" ".join([config.sip_bin, "-c", code_directory, "-b", sip_build_file, "-I", sip_directory, "PyIndimod.sip"]))

# Create the Makefile.
makefile = sipconfig.SIPModuleMakefile(config, build_file, dir=code_directory, threaded=1 )

# Add the library we are wrapping.  The name doesn't include any platform
# specific prefixes or extensions (e.g. the "lib" prefix on UNIX, or the
# ".dll" extension on Windows).
makefile.extra_libs = ["indi", "indiclient", "nova"]
makefile.extra_include_dirs=["/usr/include/libindi", "/usr/include/libnova"]

# Generate the Makefile itself.
makefile.generate()
