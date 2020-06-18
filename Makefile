# pylitproject Makefile
PROJECT	:= $(notdir $(PWD))
MK		:= mk

-include $(MK)/help.mk
-include $(MK)/python.mk
-include $(MK)/sphinx.mk
-include $(MK)/pypi.mk
-include $(MK)/version.mk
