from datetime import datetime
from typing import List, Optional


def sum_light(els: List[datetime], start_watching: Optional[datetime] = None) -> int:
    """
    how long the light bulb has been turned on
    """
    val = 0
    watch = False
    if start_watching == None:
        watch = True
    for i in range(0, len(els), 2):
        d1 = els[i]
        d2 = els[i+1]
        if watch == False:
            if start_watching >= d1 and start_watching < d2:
                d1 = start_watching
                watch = True
            elif start_watching < d1:
                watch = True
        if watch == True:
            val += (d2-d1).total_seconds()
        
    return val