#!/usr/bin/env ruby
from = line1.scan(/from:(.*?)\]/)
to = line1.scan(/to:(.*?)\]/)
flags = line1.scan(/flags:(.*?)\]/)
puts [from, to, flags].join(',')