# linear and log axes for the same plot?
# starting with the histogram example from
# http://matplotlib.org/mpl_toolkits/axes_grid/users/overview.html
import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import make_axes_locatable
import numpy as np

# Numbers from -50 to 50, with 0.1 as step
xdomain = np.arange(-50,50, 0.1)

# bottom
axMain = plt.subplot(111)
axMain.plot(xdomain, np.sin(xdomain))
axMain.set_yscale('linear')
axMain.set_ylim((0, 50))
axMain.spines['top'].set_visible(False)
axMain.xaxis.set_ticks_position('bottom')

# middle

divider = make_axes_locatable(axMain)
axmid = divider.append_axes("top", size=2.0, pad=0, sharex=axMain)
axmid.plot(xdomain, np.sin(xdomain))
axmid.set_xscale('log')
axmid.set_ylim((50, 150))
# Removes top axis line
axmid.spines['top'].set_visible(False)
axmid.xaxis.set_ticks_position('top')
plt.setp(axmid.get_xticklabels(), visible=False)
# Removes bottom axis line
axmid.spines['bottom'].set_visible(False)
axmid.xaxis.set_ticks_position('top')
plt.setp(axmid.get_xticklabels(), visible=False)


# top
divider = make_axes_locatable(axMain)
axLin = divider.append_axes("top", size=2.0, pad=0, sharex=axMain)
axLin.plot(xdomain, np.sin(xdomain))
axLin.set_xscale('linear')
axLin.set_ylim((150, 200))

# Removes bottom axis line
axLin.spines['bottom'].set_visible(False)
axLin.xaxis.set_ticks_position('top')
plt.setp(axLin.get_xticklabels(), visible=False)

plt.title('Linear above, log below')

plt.show()
