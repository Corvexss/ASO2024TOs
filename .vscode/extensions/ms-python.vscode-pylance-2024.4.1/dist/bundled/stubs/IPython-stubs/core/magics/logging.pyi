"""
This type stub file was generated by pyright.
"""

from IPython.core.magic import Magics, line_magic, magics_class

"""Implementation of magic functions for IPython's own logging.
"""
@magics_class
class LoggingMagics(Magics):
    """Magics related to all logging machinery."""
    quiet = ...
    @line_magic
    def logstart(self, parameter_s=...): # -> None:
        """Start logging anywhere in a session.

        %logstart [-o|-r|-t|-q] [log_name [log_mode]]

        If no name is given, it defaults to a file named 'ipython_log.py' in your
        current directory, in 'rotate' mode (see below).

        '%logstart name' saves to file 'name' in 'backup' mode.  It saves your
        history up to that point and then continues logging.

        %logstart takes a second optional parameter: logging mode. This can be one
        of (note that the modes are given unquoted):

        append
            Keep logging at the end of any existing file.

        backup
            Rename any existing file to name~ and start name.

        global
            Append to  a single logfile in your home directory.

        over
            Overwrite any existing log.

        rotate
            Create rotating logs: name.1~, name.2~, etc.

        Options:

          -o
            log also IPython's output. In this mode, all commands which
            generate an Out[NN] prompt are recorded to the logfile, right after
            their corresponding input line. The output lines are always
            prepended with a '#[Out]# ' marker, so that the log remains valid
            Python code.

          Since this marker is always the same, filtering only the output from
          a log is very easy, using for example a simple awk call::

            awk -F'#\\[Out\\]# ' '{if($2) {print $2}}' ipython_log.py

          -r
            log 'raw' input.  Normally, IPython's logs contain the processed
            input, so that user lines are logged in their final form, converted
            into valid Python.  For example, %Exit is logged as
            _ip.magic("Exit").  If the -r flag is given, all input is logged
            exactly as typed, with no transformations applied.

          -t
            put timestamps before each input line logged (these are put in
            comments).

          -q 
            suppress output of logstate message when logging is invoked
        """
        ...
    
    @line_magic
    def logstop(self, parameter_s=...): # -> None:
        """Fully stop logging and close log file.

        In order to start logging again, a new %logstart call needs to be made,
        possibly (though not necessarily) with a new filename, mode and other
        options."""
        ...
    
    @line_magic
    def logoff(self, parameter_s=...): # -> None:
        """Temporarily stop logging.

        You must have previously started logging."""
        ...
    
    @line_magic
    def logon(self, parameter_s=...): # -> None:
        """Restart logging.

        This function is for restarting logging which you've temporarily
        stopped with %logoff. For starting logging for the first time, you
        must use the %logstart function, which allows you to specify an
        optional log filename."""
        ...
    
    @line_magic
    def logstate(self, parameter_s=...): # -> None:
        """Print the status of the logging system."""
        ...
    


