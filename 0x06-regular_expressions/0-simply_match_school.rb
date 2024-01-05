#!/usr/bin/env ruby
#script that takes an argument and passes it to a regular expression
#to match School

puts ARGV[0].scan(/School/).join
