# helper routines to turn messages into the right
# types for displayment later
WARNING, DEBUG, CHANGE = 0x1, 0x2, 0x3
def W(s):
	return (WARNING, s)
def D(s):
	return (DEBUG, s)
def C(s):
	return (CHANGE, s)

from utils import merge_keys_to_list

# base Command class
class Command:
	@classmethod
	def parse(cls, output):
		raise Exception("not implemented for %s" % str(cls))
	@classmethod
	def compare(cls, prev, cur):
		raise Exception("not implemented for %s" % str(cls))

from .debian import *
from .files import *
from .ipc import *
from .network import *
from .processes import *
from .systemd import *
from .ubuntu import *
from .uptime import *
from .users import *
from .version import *

# commands will be executed in the order they appear in this list
COMMANDS = [
	files.CheckBootDirectoryCommand,
	files.CheckEtcDirectoryCommand,
	files.CheckForPipesCommand,
	files.FindSuidBinariesCommand,
	ipc.ListMessageQueuesCommand,
	ipc.ListSemaphoreArraysCommand,
	ipc.ListSharedMemorySegmentsCommand,
	processes.CheckProcessessCommand,
	systemd.ListSystemDServicesCommand,
	ubuntu.IsRestartRequiredCommand,
	debian.ListInstalledPackagesCommand,
	uptime.UptimeCommand,
	users.CheckGroupsCommand,
	users.CheckUsersCommand,
	version.KernelVersionCommand,
	network.ListListeningTCPUDPPortsCommand,
	ipc.ListListeningUNIXSocketsCommand
]

# built up mapping from command names to command classes
COMMAND_CACHE = {}
for cmd in COMMANDS:
	COMMAND_CACHE[cmd.name] = cmd
