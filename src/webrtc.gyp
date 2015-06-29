{
  'includes': [
    '../third_party/webrtc/src/webrtc/supplement.gypi',
    '../third_party/webrtc/src/webrtc/build/common.gypi',
    '../third_party/webrtc/src/talk/build/common.gypi',
    '../build/config.gypi',
    '../nodejs.gypi',
    'addon.gypi',
  ],
  'targets': [
    {
      'target_name': 'webrtc-native',
      'sources': [
        'Core.cc',
        'BackTrace.cc',
        'EventEmitter.cc',
        'Observers.cc',
        'Module.cc',
        'PeerConnection.cc',
        'DataChannel.cc',
        'GetSources.cc',
        'GetUserMedia.cc',
        'MediaStream.cc',
        'MediaStreamTrack.cc',
        'MediaConstraints.cc',
        'Stats.cc',
      ],
      'dependencies': [
        '<(DEPTH)/talk/libjingle.gyp:libjingle_peerconnection', 
        '<(DEPTH)/webrtc/modules/modules.gyp:video_capture_module',
        '<(DEPTH)/webrtc/modules/modules.gyp:video_capture_module_internal_impl',
        '<(DEPTH)/webrtc/modules/modules.gyp:video_render_module',
        '<(DEPTH)/webrtc/modules/modules.gyp:video_render_module_internal_impl',
      ],
      'include_dirs': [
        '<(DEPTH)/third_party/jsoncpp/source/include',
        '<(DEPTH)/third_party/libsrtp/srtp',
        '<(DEPTH)/third_party/libyuv/include',
        "<!(node -e \"require('nan')\")",
      ],
      'conditions': [ 
        ['OS=="linux"', {
          'include_dirs': [
            '/usr/include/node/',
            '/usr/include/nodejs/'
          ],
          'cflags': [
            '-Wno-deprecated-declarations',
            '-Wno-unused-variable',
            '-Wno-unknown-pragmas',
            '-Wno-unused-result',
          ],
        }],
        ['OS=="win"', {
          'msvs_disabled_warnings': [ 
            4251,
            4530,
            4702,
            4199,
            4201,
            4267,
            4005,
            4506,
            4789,
          ],
        }],
        ['OS=="mac"', {
          'xcode_settings': {
            'OTHER_CFLAGS': [
              '-Wno-deprecated-declarations',
              '-Wno-newline-eof',
              '-Wno-unknown-pragmas',
              '-Wno-unused-result',
            ],
          },
          'defines': [
            'USE_BACKTRACE',
          ],
        }],
      ],      
    },
    {
      'target_name': 'All',
      'type': 'none',
      'dependencies': [
        'webrtc-native',
      ],
    },
  ],
}
