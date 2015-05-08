#!/usr/bin/env python
# -*- coding: utf-8 vi:ts=4:noexpandtab

def options(opt):
	opt.load("compiler_c")

def configure(conf):
	conf.load("compiler_c")
	conf.check_cfg(
	 package="libpng",
	 args="--cflags --libs",
	 uselib_store="PNG",
	)
	conf.check_cfg(
	 package="libtiff-4",
	 args="--cflags --libs",
	 uselib_store="TIFF",
	)
	if conf.env.CC_NAME in ('gcc',):
		conf.env.LIB += ['m']

	conf.write_config_header('config.h')
	conf.env.INCLUDES += ['.']

def build(bld):
	bld(
	 target="tif22pnm",
	 features="c cprogram",
	 source="ptspnm.c minigimp.c miniglib.c ptstiff3.c tif22pnm.c",
	 use="TIFF",
	)
	bld(
	 target="png22pnm",
	 features="c cprogram",
	 source="png22pnm.c",
	 use="PNG",
	)
