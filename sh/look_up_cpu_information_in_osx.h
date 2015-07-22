o -n "CPU型号:    " 
sysctl -n machdep.cpu.brand_string
echo -n "CPU核心数:  " 
sysctl -n machdep.cpu.core_count
echo -n "CPU线程数:  "
sysctl -n machdep.cpu.thread_count
echo "其它信息："
system_profiler SPDisplaysDataType SPMemoryDataType SPStorageDataType | grep 'Graphics/Displays:\|Chipset Model:\|VRAM (Total):\|Resolution:\|Memory Slots:\|Size:\|Speed:\|Storage:\|Media Name:\|Medium Type:'
                                                                                    # sysctl -a | grep ".cpu."
