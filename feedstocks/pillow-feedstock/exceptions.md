#pillow
##Command '['/usr/bin/git', 'fetch', 'https://github.com/regro-cf-autotick-bot/pillow-feedstock.git']' returned non-zero exit status 128.
Traceback (most recent call last):
  File "../cf-scripts/03-auto_tick.xsh", line 284, in <module>
    hash_type=attrs.get('hash_type', 'sha256'))
  File "../cf-scripts/03-auto_tick.xsh", line 140, in run
    git fetch @(origin)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 19376, in subproc_captured_hiddenobject
    return run_subproc(cmds, captured='hiddenobject')
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 19339, in run_subproc
    command.end()
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 12645, in end
    self._end(tee_output=tee_output)
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 12664, in _end
    self._raise_subproc_error()
  File "/home/travis/mc/lib/python3.6/site-packages/xonsh/__amalgam__.py", line 12774, in _raise_subproc_error
    output=self.output)
subprocess.CalledProcessError: Command '['/usr/bin/git', 'fetch', 'https://github.com/regro-cf-autotick-bot/pillow-feedstock.git']' returned non-zero exit status 128.


