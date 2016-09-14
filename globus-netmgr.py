#! /usr/bin/python
import sys
import os
import syslog

syslog.openlog('globus-netmgr', 0, syslog.LOG_LOCAL5)

def pre_listen(task_id, transport, attrs):
    syslog.syslog('function=pre_listen,task_id=' + task_id + ',transport=' + transport)
    res = None
    for (scope, name, value) in attrs:
        syslog.syslog('scope=' + scope + ',' + name + '=' + value)
        if scope == 'python':
            if name == 'netmgr' and value != "pre_listen":
                syslog.syslog('pre_listen called when ' + value + ' expected')
                raise "pre_listen called when ", value, " expected"
            elif name == 'expected_result':
                syslog.syslog('# evaluating ' + value)
                exec value
#    syslog.syslog('res =' + res)
    return res

def post_listen(task_id, transport, local_contact, attrs):
    syslog.syslog('function=post_listen,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact)
    res = None
    for (scope, name, value) in attrs:
        syslog.syslog('scope=' + scope + ',' + name + '=' + value)
        if scope == 'python':
            if name == 'netmgr' and value != "post_listen":
                syslog.syslog('post_listen called when ' + value + ' expected')
                raise "post_listen called when ", value, " expected"
            elif name == 'expected_result':
                syslog.syslog('# evaluating ' + value)
                exec value
#    syslog.syslog('res =' + res)
    return res

def pre_accept(task_id, transport, local_contact, attrs):
    syslog.syslog('function=pre_accept,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact)
    res = None
    for (scope, name, value) in attrs:
        syslog.syslog('scope=' + scope + ',' + name + '=' + value)
        if scope == 'python':
            if name == 'netmgr' and value != "pre_accept":
                syslog.syslog('pre_accept called when ' + value + ' expected')
                raise "pre_accept called when ", value, " expected"
            elif name == 'expected_result':
                syslog.syslog('# evaluating ' + value)
                exec value
#    syslog.syslog('res =' + res)
    return res

def post_accept(task_id, transport, local_contact, remote_contact, attrs):
    syslog.syslog('function=post_accept,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact + ',remote_contact=' + remote_contact)
    syslog.syslog('event=flow,action=start,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact + ',remote_contact=' + remote_contact)
    res = None
    for (scope, name, value) in attrs:
        syslog.syslog('scope=' + scope + ',' + name + '=' + value)
        if scope == 'python':
            if name == 'netmgr' and value != "post_accept":
                syslog.syslog('post_accept called when ' + value + ' expected')
                raise "post_accept called when ", value, " expected"
            elif name == 'expected_result':
                syslog.syslog('# evaluating ' + value)
                exec value
#    syslog.syslog('res =' + res)
    return res

def pre_connect(task_id, transport, remote_contact, attrs):
    syslog.syslog('function=pre_connect,task_id=' + task_id + ',transport=' + transport + ',remote_contact=' + remote_contact)
    res = None
    for (scope, name, value) in attrs:
        syslog.syslog('scope=' + scope + ',' + name + '=' + value)
        if scope == 'python':
            if name == 'netmgr' and value != "pre_connect":
                syslog.syslog('pre_connect called when ' + value + ' expected')
                raise "pre_connect called when ", value, " expected"
            elif name == 'expected_result':
                syslog.syslog('# evaluating ' + value)
                exec value
#    syslog.syslog('res =' + res)
    return res

def post_connect(task_id, transport, local_contact, remote_contact, attrs):
    syslog.syslog('function=post_connect,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact + ',remote_contact=' + remote_contact)
    syslog.syslog('event=flow,action=start,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact + ',remote_contact=' + remote_contact)
    res = None
    for (scope, name, value) in attrs:
        syslog.syslog('scope=' + scope + ',' + name + '=' + value)
        if scope == 'python':
            if name == 'netmgr' and value != "post_connect":
                syslog.syslog('post_connect called when ' + value + ' expected')
                raise "post_connect called when ", value, " expected"
            elif name == 'expected_result':
                syslog.syslog('# evaluating ' + value)
                exec value
#    syslog.syslog('res =' + res)
    return res

def pre_close(task_id, transport, local_contact, remote_contact, attrs):
    syslog.syslog('function=pre_close,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact + ',remote_contact=' + remote_contact)
    syslog.syslog('event=flow,action=stop,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact + ',remote_contact=' + remote_contact)
    res = None
    for (scope, name, value) in attrs:
        syslog.syslog('scope=' + scope + ',' + name + '=' + value)
        if scope == 'python':
            if name == 'netmgr' and value != "pre_close":
                syslog.syslog('pre_close called when ' + value + ' expected')
                raise "pre_close called when ", value, " expected"
            elif name == 'expected_result':
                syslog.syslog('# evaluating ' + value)
                exec value
#    syslog.syslog('res =' + res)
    return res

def post_close(task_id, transport, local_contact, remote_contact, attrs):
    syslog.syslog('function=post_close,task_id=' + task_id + ',transport=' + transport + ',local_contact=' + local_contact + ',remote_contact=' + remote_contact)
    res = None
    for (scope, name, value) in attrs:
        syslog.syslog('scope=' + scope + ',' + name + '=' + value)
        if scope == 'python':
            if name == 'netmgr' and value != "post_close":
                syslog.syslog('post_close called when ' + value + ' expected')
                raise "post_close called when ", value, " expected"
            elif name == 'expected_result':
                syslog.syslog('# evaluating ' + value)
                exec value
#    syslog.syslog('res =' + res)
    return res
