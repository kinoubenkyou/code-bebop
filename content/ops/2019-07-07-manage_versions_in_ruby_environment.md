Tags: bash, ruby, gem, bundler

# Manage Ruby's Version

On your machine, there might be projects using different versions of Ruby. Installing them and using the correct one for each project is what a Ruby version manager for. The most popular managers are Rbenv and RVM.

# Manage Gems' Version

With Rbenv, each ruby version has its own separate environment to install gems to. On the other hand, it is still possible to install different version of a same gem to one ruby environment. You can install a specific version of gem with `gem install <gem-name> -v <version>`. You can also run a specific version of a gem with `<gem-binary> _<version>_`.

There is another way to manage gems' version from the local (project) point of view. This uses gem Bundler and a `Gemfile`, which is a list of gems and their corresponding version. When you are in the same directory with a `Gemfile`, you can install all the listed version of gems with `bundle install` and run each of them with `bundle exec <gem-binary>`.
