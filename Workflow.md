# Outline of workflow #

The standard workflow will be:
  * Create a new Website instance with desired settings, anything not set will use the defaults set in WebsiteDefaults
  * Create Content instances that set particular contents properties
  * Compile those Contents. Anything not in Contents will use the Website property (which, in turn uses the defaults if that isn't found (if that isn't found in the defaults, it is left as text))
  * Finished!