## We require new-style dependency handling.
AUTOMAKE_OPTIONS = 1.7

noinst_LIBRARIES = libhelper-proto.a

libhelper_proto_a_CFLAGS =	\
	$(MATE_SCREENSAVER_CFLAGS)

libhelper_proto_a_SOURCES =	\
	helper_proto.h			\
	helper_proto.c

pkglibexecdir = $(libexecdir)/mate-screensaver
pkglibexec_PROGRAMS = mate-screensaver-pam-helper

mate_screensaver_pam_helper_CFLAGS =	\
	$(MATE_SCREENSAVER_CFLAGS)

mate_screensaver_pam_helper_SOURCES =	\
	pam-helper.c

mate_screensaver_pam_helper_LDADD =	\
	libhelper-proto.a

mate_screensaver_pam_helper_LDFLAGS =	\
	$(AUTH_LIBS)
