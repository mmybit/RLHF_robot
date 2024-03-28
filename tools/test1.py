import utils

if __name__ == "__main__":
   
    parser = utils.get_parser()
    args = parser.parse_args()
    scripts = utils.get_scripts(args)